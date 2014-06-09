# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

period = 20*86400
sun = RigidSphere(6.955e8, period, [0,1,2])
# 				 lat phase area (frac of star surface area)
spots = [sun.spot(90, 0.5, 0.001), sun.spot(20, 0.2, 0.005), sun.spot(60, 0.2, 0.001)]

rt = Raytracer(sun, spots, 200)
occ = FastOccluder(sun, spots)

samples = 200
T = np.linspace(0,2*period,samples)

plt.clf()

plt.subplot(1,2,2)
plt.plot(T, get_rvs(occ, T))

plt.subplot(1,2,1)
rgb = rt.render(rt.trace(period * 0.1))
plt.axis('off')
plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.show()
