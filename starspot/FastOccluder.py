# FastOccluder.py: fast algorithm for computing RV distribution

import math
import numpy as np
from itertools import izip
from scipy.integrate import quad

import physics

class FastOccluder:
    # A fast simulator using equal-RV planes, parallel to rotation axis
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

        # integrate base attenuations
        self.base_mask = np.zeros(resolution)
        for i,(x,ymax) in enumerate( izip(self.x, self.ymax) ):
            self.base_mask[i] = quad( lambda y : physics.default_limb_darkening(math.acos(\
                                      math.sqrt(R**2 - x**2 - y**2)/R) ),\
                                      -ymax, ymax)[0]

    def trace(self, t):
        # Computes distribution of RVs at time t.
        pass