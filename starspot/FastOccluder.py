# FastOccluder.py: fast algorithm for computing RV distribution

import math
import numpy as np
from itertools import izip
from scipy.integrate import quad

import physics

class FastOccluder:
    # A fast simulator using equal-RV planes, parallel to rotation axis
    # Doesn't work when spots overlap!
    def __init__(self, target, resolution, spots=[]):
        # Constructor. Precomputes plane RVs.
        self.target = target
        self.resolution = resolution
        self.spots = spots

        # get plane RVs and grid lines
        max_rv = target.max_radvel()
        R = target.radius
        self.radvels = np.linspace(-max_rv, max_rv, resolution)
        self.x = np.linspace(-R, R, resolution)
        self.ymax = np.sqrt( R**2 - self.x**2 )

    def trace(self, t):
        # Computes distribution of RVs at time t.
        rv = 0
        for pos,theta in self.spots:
            rv -= / R**2
        return rv