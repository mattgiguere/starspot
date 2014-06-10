# fluid_demo.py: test for FluidSphere class.

import numpy as np
from starspot import *

period = 20*86400
rigid_star = RigidSphere(6.955e8, period, [0,1,0]) # uniform 20 day period
fluid_star = FluidSphere(6.955e8, period, 10*period, [0,1,0]) # 20 days at equator, 200 at poles

spots = [rigid_star.spot(0,0,0.005),
         rigid_star.spot(30,0,0.005),
         rigid_star.spot(-30,0,0.005),
         rigid_star.spot(60,0,0.005),
         rigid_star.spot(-60,0,0.005)]

rigid_rt = Raytracer(rigid_star, spots, 150)
fluid_rt = Raytracer(fluid_star, spots, 150)

plt.clf()

plt.subplot(1,2,1) # plot rigid
rgb = rigid_rt.render( rigid_rt.trace(200000) )
plt.axis('off')
plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.subplot(1,2,2) # plot fluid
rgb = fluid_rt.render( fluid_rt.trace(200000) )
plt.axis('off')
plt.imshow(rgb, interpolation='nearest', origin='lower')

plt.show()