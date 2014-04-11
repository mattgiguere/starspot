# render.py: render demo for starspot library.

import numpy as np
from starspot import *

sun = RigidSphere(6.955e8, 24*86400, [0,1,0])
spots = [sun.spot(45,0.2,4e7)]
rt = Raytracer(sun, 200, spots)
rgb = rt.render(0)

plt.clf()
plt.cla()
plt.imshow(rgb, interpolation='nearest')
plt.show()
