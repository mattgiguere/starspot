# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 20*86400, [0,1,0])
spots = [sun.spot(0,1,20e7)]
sim = Simulation(sun, 50, spots)

# render at a time
def rt(t):
    rgb = sim.render(t)

    plt.subplot(3,1,1)
    plt.cla()
    plt.imshow(rgb, interpolation='nearest')

    plt.subplot(3,1,2)
    x = np.linspace(0,1,1000)
    base = physics.voigt(x, 1, 0.5, 0.1, 0)
    plt.plot(x, base, label='base', color='gray')

    ret = np.zeros( base.shape )
    mask = sim.compute_mask(t)
    for rv, m in zip(sim.radvels, mask):
        ret += m * physics.voigt(x + rv/10000.0, 1, 0.5, 0.1, 0)
    ret /= mask.sum()
    plt.plot(x, ret, label='spread', color='red')

    plt.axvline(0.5, color='gray')
    plt.axvline(x[np.argmax(ret)], color='red')

    plt.legend( ('base', 'spread') )

    return np.average(x, weights=ret)

plt.clf()
rt(0)

T = np.linspace(0,2000000,100)
rv = []
for t in T:
    print t
    rv.append(rt(t))

RV = np.array(rv)

plt.subplot(3,1,3)
plt.plot(T,RV)
plt.show()
