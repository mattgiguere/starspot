# profile.py: code profiling

import cProfile
import pstats

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

NTIMES = 200
NSIMS = 300

T = np.linspace(0, 40. * 86400., NTIMES)
L = np.linspace(-90, 90, NSIMS)

def f():
    for lat in L:
        sun = RigidSphere(6.955e8, 20. * 86400., [0,1,1])
        spots = [sun.spot(lat,0.5,0.001)]
        occ = FastOccluder(sun, spots)
        get_rvs(occ, T)
    
cProfile.run('f()', 'build/rv_profile_stats')

p = pstats.Stats('build/rv_profile_stats')
p.strip_dirs()
p.sort_stats('cumulative')
p.print_stats()