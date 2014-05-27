# Written by Aida Behmard, 5/22/2014
# Program that adds random coverage by starspots (1.5-141 MSH)
# Refer to Jeffers et al. (2014)

import numpy as np
import math
import random 
import matplotlib.pyplot as plt
from scipy import stats 

class RandomSpots:
	# areas, locations, brightness/sharpness 

	def lognorm(M, s, N): 
	# M = median, s = stand dev, N = number
	# lognormal area distribution 
	# Bogdan et al. (1988) --> Hathaway & Choundary. (2008)

		mu = np.log(M) # mean of log(x)
		sigma = np.log(s) # standard deviation of log(x)
		shape = sigma # scipy's shape parameter
	    scale = np.exp(mu) # scipy's scale parameter
	    median = np.exp(mu)
	    mode = np.exp(mu - sigma**2) 
	    mean = np.exp(mu + (sigma**2/2))  
	    x = np.linspace(0.1, 25, num = N) # values for x-axis
	    pdf = stats.lognorm.pdf(x, shape, loc = 0, scale = scale) 
	    plt.plot(x, pdf)
	    print "spot area", pdf # Random area values 
    
    def position(N):
	    # Random longitude values
	    longitude = np.random.uniform(0, 360, N) # values in a 2x3 array
	    print "longitude", longitude

	    # Random latitude values
	    x = np.random.uniform(0.0, 1.0, N)
	    lat = math.asin(2*x+1)
	    print "latitude", lat

	    
	    # Bogdan et al. (1998) 




