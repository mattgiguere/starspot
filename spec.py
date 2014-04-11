# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 20*86400, [0,1,2])
spots = [sun.spot(60,0,20e7)]
rt = Raytracer(sun, 70, spots)

# simulate RV measurement with Voigt spectra at a time
def slow_rv(t):
    mask = rt.trace(t)
    rgb = rt.render(mask)

    x = np.linspace(0,1,1000)
    base = physics.voigt(x, 1, 0.5, 0.1, 0)

    ret = np.zeros( base.shape )
    for rv, m in zip(rt.radvels, mask):
        ret += m * physics.voigt(x + rv/10000.0, 1, 0.5, 0.1, 0)
    ret /= mask.sum()

    return np.average(x, weights=ret)

# simulate RV measurement with weighted average
def fast_rv(t):
    mask = rt.trace(t)
    return rt.mean_radvel(mask)

plt.clf()

T = np.linspace(0,4000000,100)
rv = []
for t in T:
    print t
    rv.append(fast_rv(t))

RV = np.array(rv)

plt.plot(T,RV)
plt.show()
