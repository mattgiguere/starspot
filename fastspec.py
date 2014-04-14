# fastspec.py: spectrum demo using fast occluder.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 20*86400, [0,1,0])
spots = [sun.spot(0,1,0.01)]
occ = FastOccluder(sun, 100, spots)

plt.clf()
plt.plot(occ.base_mask)
plt.show()