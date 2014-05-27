# Written by Aida Behmard, 5/22/2014
# Program that adds random coverage by small starspots (1.5-141 MSH)
# Refer to Jeffers et al. (2014)

import numpy as np
import math
import random 
from scipy import stats 

def lognorm():
	M = float(4) # geometric mean == median
	s = float(2) # geometric standard deviation
	mu = np.log(M) # mean of log(x)
	sigma = np.log(s) # standard deviation of log(x)
	shape = sigma # scipy's shape parameter
	scale = np.exp(mu) # scipy's scale parameter
	median = np.exp(mu)
	mode = np.exp(mu - sigma**2) # note that mode depends on both M and s
	mean = np.exp(mu + (sigma**2/2)) # values for x-axis 
	x = np.linspace(0.1, 25, num = 400) # values for x-axis
	pdf = stats.lognorm.pdf(x, shape, loc = 0, scale = scale) # probability distribution






def random():
	# Obtain random longitude values
	longitude = np.random.uniform(0,360,[2,3]) # values in a 2x3 array
	print "Spot Longitude", longitude

	# Obtain random latitude values
	x = np.random.uniform(0.0,1.0, [2,3])
	lat = math.asin(2*x+1)
	print "Spot Latitude", lat

	# Obtain random spot radius values
	# Bogdan et al. (1998) 




