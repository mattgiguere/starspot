# geometry.py: geometric utilities

import numpy as np
import math

# rotate by angle (radians) around axis
def rotation_matrix(angle, direction):
    sina = math.sin(angle)
    cosa = math.cos(angle)
    R = np.diag([cosa, cosa, cosa])
    R += np.outer(direction, direction) * (1.0 - cosa)
    d = direction * sina
    R += np.array([[ 0.0, -d[2], d[1]],
                   [ d[2], 0.0, -d[0]],
                   [-d[1], d[0], 0.0]])
    return R

# standard inclined axis vector (degrees)
# 0 = edge-on, 90 = face-on
def inclined_axis(angle):
    angle *= math.pi/180.
    return [0, math.cos(angle), math.sin(angle)]

# (R, half angle) -> spherical cap area
def cap_area(R, theta):
    return 2. * math.pi * R**2 * (1 - math.cos(theta))

# half angle -> cap area / sphere area
def frac_cap_area(theta):
    return 0.5 * (1 - math.cos(theta))

# cap area / sphere area -> half angle (inverse of frac_cap_area)
def cap_half_angle(fracarea):
    return math.acos(1. - 2.*fracarea)

# given array of normalized (x,y,z) points and axis, convert to 1D array of latitudes
def points_to_latitudes(points, axis):
    return np.arccos( np.dot(points, axis) )
