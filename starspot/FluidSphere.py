# Written by Aida Behmard, 6/3/2014
# FluidSphere.py: fluid spherical model of a star
# Accomadates differential angular velocities for spots ar different latitudes

## Diff. rotation velocity notes ##
# - Ref: "Living Reviews in Solar Physics"
# - Donati  & Collier Cameron (1997):
# - AB Doradus => K dwarf
# - eq_rate = 12.2434 rad/d; diff_rate = 0.0564 rad/d

# ASSUMING that period(theta) has problems 

import numpy as np
import math
import geometry
import random
import physics

class FluidSphere:
    # Fluid sphere model of a star.
    # A star is a sphere at (0,0,0). The observer looks in the -z direction.
    # Rotation inclination is given by an angular velocity vector (numpy 3-array)
    # -----------------------------------------------------------------------------

    def __init__(self, radius, eq_period, polar_period, axis):
        # Constructor. Builds angular velocity vector using period and axis.
        self.radius = radius
        self.axis = np.array(axis)
        self.axis = self.axis / np.linalg.norm(self.axis)
        self.eq_angvel = 2*math.pi / eq_period
        self.polar_angvel = 2*math.pi / polar_period
        self.scalar_angvel = max( self.eq_angvel, self.polar_angvel )

    def angvel(self, points):
        # Takes points to angular velocities. Trivial constant function in this case.
        lats = geometry.points_to_latitudes(points/self.radius, self.axis)
        vels = physics.fluid_rotation(self.eq_angvel, self.polar_angvel, lats)
        return np.kron(self.axis, vels.reshape(len(vels), 1))

    def max_radvel(self):
        # Magnitude of RV at star's edge (accounting for inclination).
        sini = math.sqrt( 1 - self.axis[2]**2 )
        return self.scalar_angvel * self.radius * sini

    def evolve(self, points, t):
        # Given points at time 0, return points at time t.
        lats = geometry.points_to_latitudes(points/self.radius, self.axis)
        vels = physics.fluid_rotation(self.eq_angvel, self.polar_angvel, lats)
        result = np.zeros(points.shape)

        mat = geometry.rotation_matrix(-vels * t, self.axis)
        return np.dot( points, mat.transpose() )

    def occlude(self, pos, theta, points):
        # Return a boolean mask of occluded points.
        cosines = np.dot( points/self.radius, pos/self.radius )
        return cosines >= math.cos(theta)

    # -----------------------------------------------------------------------------

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
