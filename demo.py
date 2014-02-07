# demo.py: Demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 24*86400, np.array([1,1,1])  )
sim = Simulation(sun, 100)
rgb = sim.render()
plt.clf()
plt.imshow(rgb)
plt.show()
