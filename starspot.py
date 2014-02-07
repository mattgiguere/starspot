# starspot.py: Library for starspot apparent RV simulator.

##### DEPENDENCIES #####

import numpy as np
import matplotlib.pyplot as plt
import math

##### CORE OBJECTS #####

class RigidSphere:
    """ Target star properties, in SI units.
    A star is a sphere at (0,0,0). The observer looks in the -z direction.
    Rotation inclination is given by an angular velocity vector (numpy 3-array)
    """
    def __init__(self, radius, period, axis):
        self.radius = radius
        self.angvel = (2*math.pi / period) * axis / np.sqrt( axis.dot(axis) )

    def collide(self, points):
        # Ray collider.
        # In: array of query points (x,y), shape (2,N,N)
        # Out: hit points (x,y,z), with their original indices

        z2 = self.radius**2 - points[0]**2 - points[1]**2
        hits = (z2 > 0)
        indices = np.nonzero(hits)
        z = np.sqrt( z2[hits] )

        out_points = np.vstack([points[0][hits], points[1][hits], z]).transpose()
        return out_points, indices

    def tangvel(self, points):
        # Takes (x,y,z) surface points to angular velocities.
        return np.cross( self.angvel, points )

class Simulation:
    """ A simulation instance, keeping precomputed information. """
    def __init__(self, target, resolution):
        self.target = target
        self.resolution = resolution

        # get query points and collide them
        R = target.radius
        res = resolution
        grid_points = np.mgrid[ R:-R:res*1j, -R:R:res*1j ]
        self.points, self.pixels = target.collide(grid_points)

        # get RV
        self.radvel = -target.tangvel(self.points)[:,2]

    def render(self):
        rgb = np.zeros((self.resolution, self.resolution, 3))

        # scale RVs
        rv_scale = 1+np.max( np.abs(self.radvel) )

        for y,x,rv in zip(self.pixels[0], self.pixels[1], self.radvel):
            if rv<0: # blueshift
                rgb[x,y,2] = 1
                rgb[x,y,0] = rgb[x,y,1] = 1+rv/rv_scale
            else: # redshift
                rgb[x,y,0] = 1
                rgb[x,y,1] = rgb[x,y,2] = 1-rv/rv_scale

        return rgb 
