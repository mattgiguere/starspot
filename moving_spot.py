# Attempt to model star spot movement 

import pylab
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

### Star Surface ###

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(theta), np.sin(phi))
y = 10 * np.outer(np.sin(theta), np.sin(phi))
z = 10 * np.outer(np.ones(np.size(theta)), np.cos(phi))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')

plt.show()

# variable to put in demo: p1, p2, lat1, time

def spot_equation(lat1, long1):
    # convert latitude and longitude to 
    # spherical coordinates in radians
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    spot_phi = (90.0 - lat1)*degrees_to_radians
    
    # theta = longitude
    spot_theta = long1*degrees_to_radians

    spot_equation = (spot_phi, spot_theta)


# fill in p1 & p2
p1 = -1.469 
p2 = 108.3  
p3 = 20
for time in range(1,11):
	lat1 = (p1*time**2 + p2*time + p3)
	# fill in long1 value
	long1 = 20 
	print spot_equation(lat1, long1) # gives spot position (phi, theta)
	# plt.plot(x, y, z): something like this in terms of Cartesian?


