# FastOccluder.py: fast algorithm for computing RV distribution

import math
from itertools import izip
from scipy.integrate import quad
from SpotDecay import *

import physics
import geometry

class FastOccluder:
    # A fast simulator using equal-RV planes, parallel to rotation axis
    # Doesn't work when spots overlap!
    def __init__(self, target, spots=[]):
        # Constructor. Precomputes plane RVs.
        self.target = target
        self.spots = spots
        self.max_rv = target.max_radvel()

    def rv(self, t): # area => spot area
        # Computes approximate mean RV time t.
        rv_all = 0
        for pos,fracarea in self.spots:
            pos_t = self.target.evolve(pos, -t) / self.target.radius
            if pos_t[2] < 0:
                # behind star
                continue

            if hasattr(fracarea, '__call__'): # is fracarea a lambda?
                theta = geometry.cap_half_angle( fracarea(t) )
            else: # or a constant
                theta = geometry.cap_half_angle( fracarea )

            area = math.pi * math.sin(theta)**2
            area *= math.sqrt(1 - pos_t[0]**2 - pos_t[1]**2 ) # perspective

            R = self.target.radius
            rv = self.max_rv * pos_t[0]
            ld = physics.default_limb_darkening(math.acos( pos_t[2] ))
            rv_all -= area * rv * ld
        return rv_all
