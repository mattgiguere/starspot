# Raytracer.py: slow raytracing simulator

import numpy as np
import math
from itertools import izip

import physics

class Raytracer:
    # A raytracer simulation instance, keeping precomputed information.
    # Target is assumed to be a sphere, with property radius.
    def __init__(self, target, resolution, spots = []):
        # Constructor. Precomputes ray hits.
        self.target = target
        self.resolution = resolution
        self.spots = spots

        # make grid of rays
        R = target.radius
        res = resolution
        grid = np.mgrid[ -R:R:res*1j, -R:R:res*1j ]

        # collide rays with sphere
        z2 = target.radius**2 - grid[0]**2 - grid[1]**2
        hits = (z2 > 0)
        z = np.sqrt( z2[hits] )

        # save positions of hit pixels, and hit locations
        self.pixels = np.nonzero(hits)
        self.points = np.vstack([grid[0][hits], grid[1][hits], z]).transpose()

        # get TV = AV x r, RV = -z . TV
        angvels = target.angvel(self.points)
        tangvels = np.cross(angvels, self.points)
        self.radvels = -tangvels[:,2]

        # get base luminosity mask from limb darkening
        norms = np.apply_along_axis(np.linalg.norm, 1, self.points)
        thetas = np.arccos( self.points[:,2] / norms )
        self.base_mask = physics.default_limb_darkening( thetas )

    def trace(self, t):
        # Computes attenuations at all points at time t.
        mask = np.copy( self.base_mask )
        for pos,theta in self.spots:
            pos_t = self.target.evolve(pos, -t)
            mask[ self.target.occlude(pos_t, theta, self.points) ] *= 0.1
        return mask

    def mean_rv(self, mask):
        # Computes apparent RV at with attenuation mask.
        return np.average( self.radvels, weights=mask )

    def rv(self, t):
        # Computes apparent RV at time t.
        return self.mean_rv( self.trace(t) )

    def render(self, mask):
        # Render this instance at time t.
        rgb = np.zeros((self.resolution, self.resolution, 3))

        # scale RVs
        rv_scale = 1+np.max( np.abs(self.radvels) )
        for y,x,rv,atten in izip(self.pixels[0], self.pixels[1], self.radvels, mask):
            if rv<0: # blueshift
                rgb[x,y,2] = 1
                rgb[x,y,0] = rgb[x,y,1] = 1+rv/rv_scale
            else: # redshift
                rgb[x,y,0] = 1
                rgb[x,y,1] = rgb[x,y,2] = 1-rv/rv_scale
            rgb[x,y,:] *= atten * 1.2 * math.pi

        return rgb
