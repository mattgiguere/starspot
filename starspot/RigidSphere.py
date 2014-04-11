# RigidSphere.py: non-fluid spherical model of a star

import numpy as np
import matplotlib.pyplot as plt
import math

from . import geometry

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
        mat = geometry.rotation_matrix(self.scalar_angvel * t, self.axis)
        return np.dot( points, mat.transpose() )

    def spot(self, theta, phase, size):
        # Given spherical coords, get absolute coords
        # TODO(Cyril): finish this
        return np.array([0,0,self.radius,size])
