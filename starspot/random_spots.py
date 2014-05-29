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

	def lognorm(mu, s, N): 
	# mu = mean of ln(A), s = sigma of ln(A), N = expected number of spots
	# Bogdan et al. (1988) --> Hathaway & Choundary (2008)

		shape = s # scipy's shape parameter
		scale = np.exp(mu) # scipy's scale parameter
		median = np.exp(mu)
		mode = np.exp(mu - s**2) 
		mean = np.exp(mu + (s**2/2))  
		A = np.linspace(1.5, 141, num = 400) # values for x-axis
		number = stats.lognorm.pdf(A, shape, loc = 0, scale = scale) 
		plt.plot(A, number)
		areas = np.random.lognormal(mu, s, N)
		print "areas:", areas # MSH

		# make in terms of fracarea
		fracearas = areas/(6.1*10**12)
		print "Fractional Spot Areas", fracareas 

	def position(N):
	    # Random longitude values
	    longitude = np.random.uniform(0, 360, N) # values in a 2x3 array
	    print "longitude:", longitude

	    # Random latitude values
	    x = np.random.uniform(0.0, 1.0, N)
	    lat = math.asin(2*x+1)
	    print "latitude:", lat

	
	
	    




