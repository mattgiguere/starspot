# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

period = 20*86400
sun = RigidSphere(6.955e8, period, [0,1,2])
spots = [sun.spot(60,0.5,0.001)]

rt = Raytracer(sun, spots, 70)
rt_hi = Raytracer(sun, spots, 200)
occ = FastOccluder(sun, spots)

samples = 200
T = np.linspace(0,2*period,samples)

plt.clf()

plt.plot(T, get_rvs(rt, T), label="old (res=70)")
plt.plot(T, get_rvs(rt_hi, T), label="old (res=200)")
plt.plot(T, get_rvs(occ, T), label="new")

plt.legend()

plt.show()
