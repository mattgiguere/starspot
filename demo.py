# demo.py: Demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 24*86400, [1,1,1])
spots = [sun.spot(0,1,1e7), sun.spot(0,1,2e7)]
sim = Simulation(sun, 200, spots)
rgb = sim.render(0)

plt.clf()
plt.imshow(rgb)
plt.show()
