# RigidSphere.py: non-fluid spherical model of a star

import numpy as np
import math
import geometry

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

    def max_radvel(self):
        # Magnitude of RV at star's edge (accounting for inclination).
        sini = math.sqrt( 1 - self.axis[2]**2 )
        return self.scalar_angvel * self.radius * sini

    def evolve(self, points, t):
        # Given points at time 0, return points at time t.
        mat = geometry.rotation_matrix(-self.scalar_angvel * t, self.axis)
        return np.dot( points, mat.transpose() )

    def occlude(self, pos, theta, points):
        # Return a boolean mask of occluded points.
        cosines = np.dot( points/self.radius, pos/self.radius )
        return cosines >= math.cos(theta)

    def spot(self, theta, phase, fracarea):
        # Given spherical coords, get absolute coords
        # Convention: theta is a latitude in degrees: 0 = equator, +90 = north pole
        # Phase is in periods: 0 = transit, 0.5 = opposition, 1 = next transit

        # find axis with z projection removed
        w = self.axis[0:2] / np.sqrt(self.axis[0]**2 + self.axis[1]**2)
        
        # apply inclination
        theta *= math.pi/180.0
        theta -= math.asin(self.axis[2])

        # get location at phase 0 (latitude only)
        c, s = math.cos(theta), math.sin(theta)
        p = self.radius * np.array( [s*w[0], s*w[1], c] )

        # rotate to phase
        mat = geometry.rotation_matrix(-2.0 * math.pi * phase, self.axis)
        p = np.dot(p, mat.transpose())

        return (p, geometry.cap_half_angle(fracarea))


   