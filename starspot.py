# starspot.py: Library for starspot apparent RV simulator.

# Notes:
#   - Simulation takes a black box as its parameter 'target'.
#   - This black box should deal with its own RV, coords, and spots.
#   - Spots are initialized by (colatitude, phase) at time 0, in degrees.
#   - But they're converted to rectangular coordinates.
#   - No class for spots: they're just arrays [x y z size] 

##### DEPENDENCIES #####

import numpy as np
import matplotlib.pyplot as plt
import math

##### PHYSICAL MODEL #####

class physics:
    # Namespace for various physical model formulas.
    @staticmethod
    def eddington_darkening(theta):
        # Computes limb darkening factor.
        # Eddington approximation method, Carroll & Ostlie (ch. 9, p. 266)
        # In: Incidence angle (ray to normal)
        # Out: Attenuation factor (0 to 1)
        return 0.4 + 0.6 * np.cos(theta)

    # Set default limb darkening formula here
    default_limb_darkening = eddington_darkening

##### CORE OBJECTS #####

class RigidSphere:
    # Rigid sphere model of a star.
    # A star is a sphere at (0,0,0). The observer looks in the -z direction.
    # Rotation inclination is given by an angular velocity vector (numpy 3-array)

    def __init__(self, radius, period, axis):
        # Constructor. Builds angular velocity vector using period and axis.
        self.radius = radius
        self.axis = np.array(axis)
        self.axis = self.axis / np.linalg.norm(self.axis)
        self.scalar_angvel = 2*math.pi / period
        self.const_angvel = self.scalar_angvel * self.axis

    def angvel(self, points):
        # Takes points to angular velocities. Trivial constant function in this case.
        return np.tile( self.const_angvel, (points.shape[0], 1) )

    def evolve(self, points, t):
        # Given points at time 0, return points at time t.
        mat = rotation_matrix(self.scalar_angvel * t, self.axis)
        return np.dot( points, mat.transpose() )

    def spot(self, theta, phase, size):
        # Given spherical coords, get absolute coords
        return np.array([0,0,self.radius,size])

class Simulation:
    # A simulation instance, keeping precomputed information.
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
        mask = self.base_mask
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

##### UTILITIES #####

def rotation_matrix(angle, direction):
    sina = math.sin(angle)
    cosa = math.cos(angle)
    R = np.diag([cosa, cosa, cosa])
    R += np.outer(direction, direction) * (1.0 - cosa)
    direction *= sina
    R += np.array([[ 0.0,         -direction[2],  direction[1]],
                      [ direction[2], 0.0,          -direction[0]],
                      [-direction[1], direction[0],  0.0]])
    return R
