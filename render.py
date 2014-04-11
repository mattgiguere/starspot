# render.py: render demo for starspot library.

import numpy as np
from starspot import *

period = 24.*86400.
sun = RigidSphere(6.955e8, period, [1,1,1])
spots = [sun.spot(0,0,10e7)]
rt = Raytracer(sun, 100, spots)

plt.clf()

for i in range(5):
    plt.subplot(1,5,i+1)
    rgb = rt.render(rt.trace(i*200000))
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.show()
