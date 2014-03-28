# render.py: render demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 24*86400, [0,0,1])
spots = [sun.spot(0,1,4e7)]
sim = Simulation(sun, 200, spots)
rgb = sim.render(200000)

plt.clf()
plt.imshow(rgb, interpolation='nearest')
plt.show()
