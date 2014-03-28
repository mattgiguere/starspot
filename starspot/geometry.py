# geometry.py: geometric utilities

import numpy as np
import math

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
