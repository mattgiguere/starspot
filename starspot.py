# starspot.py: Library for starspot apparent RV simulator.

##### DEPENDENCIES #####

import numpy as np
import matplotlib.pyplot as plt
import math

##### CORE OBJECTS #####

class RigidSphere:
    # Rigid sphere model of a star.
    # A star is a sphere at (0,0,0). The observer looks in the -z direction.
    # Rotation inclination is given by an angular velocity vector (numpy 3-array)

    def __init__(self, radius, period, axis):
        # Constructor. Builds angular velocity vector using period and axis.
        self.radius = radius
        self.const_angvel = (2*math.pi / period) * axis / np.sqrt( axis.dot(axis) )

    def angvel(self, points):
        # Takes points to angular velocities. Trivial constant function in this case.
        return np.tile( self.const_angvel, (points.shape[0], 1) )

class Simulation:
    # A simulation instance, keeping precomputed information.
    # Target is assumed to be a sphere, with property radius.
    def __init__(self, target, resolution):
        # Constructor. Precomputes ray hits.
        self.target = target
        self.resolution = resolution

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

    def compute_mask(self, t):
        # Computes luminosity weights at time t.
        return None

    def mean_radvel(self, t):
        # Computes apparent RV at time t.
        return None

    def render(self, t):
        # Render this instance at time t.
        rgb = np.zeros((self.resolution, self.resolution, 3))

        # scale RVs
        rv_scale = 1+np.max( np.abs(self.radvels) )
        for y,x,rv in zip(self.pixels[0], self.pixels[1], self.radvels):
            if rv<0: # blueshift
                rgb[x,y,2] = 1
                rgb[x,y,0] = rgb[x,y,1] = 1+rv/rv_scale
            else: # redshift
                rgb[x,y,0] = 1
                rgb[x,y,1] = rgb[x,y,2] = 1-rv/rv_scale

        return rgb 

class physics:
    # namespace for physical models
    def compute_limb_darkening(theta):
        # Computes limb darkening factor.
        # Eddington approximation method, Carroll & Ostlie (ch. 9, p. 266)
        return 0.6 + 0.4 * np.cos(theta)
