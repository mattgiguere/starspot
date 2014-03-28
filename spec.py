# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 20*86400, [0,1,1])
spots = [sun.spot(0,1,8e7)]
sim = Simulation(sun, 100, spots)

# render at a time
def rt(t):
    rgb = sim.render(t)

    plt.clf()

    plt.subplot(1,2,1)
    plt.cla()
    plt.imshow(rgb, interpolation='nearest')

    plt.subplot(1,2,2)
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
    plt.show()

rt(0)
