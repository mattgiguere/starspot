# Written by Aida Behmard, 5/22/2014
# Program that adds random coverage by starspots (1.5-141 MSH)
# Refer to Jeffers et al. (2014)

import numpy as np
import math
import random 
import matplotlib.pyplot as plt
from scipy import stats 

class RandomSpots:
	# Areas & Locations 

	def lognorm(M, s, N): 
	# M = mu, s = sigma, N = expected number of spots
	# lognormal area distribution 
	# Bogdan et al. (1988) --> Hathaway & Choundary. (2008)

		shape = s # scipy's shape parameter
		scale = np.exp(M) # scipy's scale parameter
		median = np.exp(M)
		mode = np.exp(M - s**2) 
		mean = np.exp(M + (s**2/2))  
		area = np.linspace(1.5, 141, num = 400) # values for x-axis
		number = stats.lognorm.pdf(area, shape, loc = 0, scale = scale) 
		plt.plot(area, number)

		print "area, number:", area, number

	def position(N):
	    # Random longitude values
	    longitude = np.random.uniform(0, 360, N) # values in a 2x3 array
	    print "longitude:", longitude

	    # Random latitude values
	    x = np.random.uniform(0.0, 1.0, N)
	    lat = math.asin(2*x+1)
	    print "latitude:", lat

	
	    




