# Raytracer.py: slow raytracing simulator

import numpy as np
import matplotlib.pyplot as plt
import math

from . import physics
from . import geometry

class Raytracer:
    # A raytracer simulation instance, keeping precomputed information.
    # Target is assumed to be a sphere, with property radius.
    def __init__(self, target, resolution, spots):
        # Constructor. Precomputes ray hits.
        self.target = target
        self.resolution = resolution

        spots = np.array(spots)
        self.spot_centers = spots[:,0:3]
        self.spot_sizes = spots[:,3]

        # make grid of rays
        R = target.radius
        res = resolution
        grid = np.mgrid[ R:-R:res*1j, -R:R:res*1j ]

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

    def compute_mask(self, t):
        # Computes attenuations at all points at time t.
        mask = np.copy( self.base_mask )
        for pos,size in zip(self.spot_centers, self.spot_sizes):
            r = pos - self.target.evolve(self.points, t)
            norms = np.apply_along_axis(np.linalg.norm, 1, r)
            mask[norms <= size] *= 0.1
        return mask

    def mean_radvel(self, t):
        # Computes apparent RV at time t.
        return np.average( self.radvels, weights=self.compute_mask(t) )

    def render(self, t):
        # Render this instance at time t.
        rgb = np.zeros((self.resolution, self.resolution, 3))
        mask = self.compute_mask(t)

        # scale RVs
        rv_scale = 1+np.max( np.abs(self.radvels) )
        for y,x,rv,atten in zip(self.pixels[0], self.pixels[1], self.radvels, mask):
            if rv<0: # blueshift
                rgb[x,y,2] = 1
                rgb[x,y,0] = rgb[x,y,1] = 1+rv/rv_scale
            else: # redshift
                rgb[x,y,0] = 1
                rgb[x,y,1] = rgb[x,y,2] = 1-rv/rv_scale
            rgb[x,y,:] *= atten

        return rgb 
