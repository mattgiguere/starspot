# demo.py: Demo for starspot library.

import numpy as np
from starspot import *
from visual import *
from visual.graph import *

sun = RigidSphere(6.955e8, 24*86400, [1,1,1])
#spots = [sun.spot(0,1,4e7)]
sim = Simulation(sun, 200, spots)
rgb = sim.render(400000)

plt.clf()
plt.imshow(rgb)
plt.show()
