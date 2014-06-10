# starspot.py: Library for starspot apparent RV simulator.

# Notes:
#   - Simulation takes a black box as its parameter 'target'.
#   - This black box should deal with its own RV, coords, and spots.
#   - Spots are initialized by (colatitude, phase) at time 0, in degrees.
#   - But they're converted to rectangular coordinates.
#   - No class for spots: they're just arrays [x y z size] 

import numpy as np
import matplotlib.pyplot as plt
import math

from FluidSphere import *
from RigidSphere import *
from Raytracer import *
from FastOccluder import *

def get_rvs(sim, T, verbose=False):
    # takes a simulation object, and returns RV time series
    if verbose:
        print "begin trace"

    rv = np.zeros( len(T) )
    for i,t in enumerate(T):
        if verbose:
            print "trace %d/%d (t=%f)" % (i+1, len(T), t)
        rv[i] = sim.rv(t)
    return rv
