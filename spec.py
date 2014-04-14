# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

period = 20*86400
sun = RigidSphere(6.955e8, period, [0,1,2])
spots = [sun.spot(45,0.5,0.01)]

rt = Raytracer(sun, spots, 100)
occ = FastOccluder(sun, spots)

renders = 5
samples = 60
T = np.linspace(0,period,samples)

plt.clf()
plt.subplot2grid((2,renders),(0,0), colspan=5)
plt.plot(T, get_rvs(occ, T))
plt.plot(T, get_rvs(rt, T))

for i in range(renders):
    plt.subplot2grid((2,renders),(1,i))
    print "render %d/%d" % (i+1, renders)
    t = 0.2*period*i/renders
    rgb = rt.render( rt.trace(t) )
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.show()
