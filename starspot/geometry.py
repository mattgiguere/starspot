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