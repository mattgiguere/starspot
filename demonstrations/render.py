# render.py: render demo for starspot library.

import numpy as np
from starspot import *

period = 24.*86400.
sun = RigidSphere(6.955e8, period, [0,1,0])
spots = [sun.spot(0,0,0.005)]
rt = Raytracer(sun, spots, 100)

plt.clf()

for i in range(5):
    plt.subplot(1,5,i+1)
    rgb = rt.render(rt.trace(i*200000))
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.show()
