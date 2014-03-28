# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 24*86400, [0,1,1])
spots = [sun.spot(0,1,4e7)]
sim = Simulation(sun, 50, spots)

def render_time(t):
    rgb = sim.render(t)

    plt.clf()

    plt.subplot(1,2,1)
    plt.cla()
    plt.imshow(rgb, interpolation='nearest')

    plt.subplot(1,2,2)
    x = np.linspace(0,1,100)
    base = physics.voigt(x, 1, 0.5, 0.1, 0)
    plt.plot(x, base, label='base')
    plt.legend( ('base') )

    plt.show()
