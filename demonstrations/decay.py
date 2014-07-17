# decay.py: spot decay demo

import numpy as np
from starspot import *

samples = 600
frames = 100
period = 20*86400
T = np.linspace(0, period, samples)
sun = RigidSphere(6.955e8, period, [0,1,0])

plt.clf()

########## no spot decay ##########

spots = [sun.spot(0,0,0.005)]
rt = Raytracer(sun, spots, 100)

for i in range(5):
    plt.subplot(2,6,i+1)
    rgb = rt.render(rt.trace(i*100000))
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

# plot RV profile
plt.subplot(2,6,6)
occ = FastOccluder(sun, spots)
plt.plot(T, get_rvs(occ,T))

########## with spot decay ##########
def simple_decay(t):
    return max(0, 0.005 * (1 - t/500000.0));

spots = [sun.spot(0,0,lambda t: simple_decay(t))]
rt = Raytracer(sun, spots, 100)

for i in range(5):
    plt.subplot(2,6,6+i+1)
    rgb = rt.render(rt.trace(i*100000))
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

# plot RV profile
plt.subplot(2,6,12)
occ = FastOccluder(sun, spots)
plt.plot(T, get_rvs(occ,T))

plt.show()
