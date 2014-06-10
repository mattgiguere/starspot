# Written by Aida Behmard, 6/4/2014
# Smoothes raw RV data 
# "wiener_filter(t)"

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener 

data = np.load('cutdata.npy') # example

t = data[:,0]
y = data[:,1]
y_smooth = data[:,3]

def wiener_filter(time):

	rv_err = data[:,2]

	# Compute variance from given RV errors
	variance = sum(x*x for x in rv_err) / 228 # N = 228
	y_wiener = wiener(data[:,1], 600, variance) # wiener(im, box_size, noise)

	# Using Wiener filter
	plt.figure(1)
	plt.subplot(211)
	plt.plot(time, y, 'o', color = 'b', label = 'Raw')
	plt.plot(time, y, color = 'b') # raw RV data

	plt.plot(time, y_wiener, 'o', color = 'r', label = 'Wiener') # smooth RV data
	plt.legend(loc='lower right', numpoints = 1)

	plt.title('Tau Ceti: Wiener Filter')
	plt.xlabel('JD - 2.44e6')
	plt.ylabel('RV (m/s)')

    # Using default smooth data
	plt.subplot(212)
	plt.plot(time, y, 'o', color = 'b', label = 'Raw')
	plt.plot(time, y, color = 'b') # raw RV data

	plt.plot(time, y_smooth, 'o', color = 'r', label = 'Default Smooth') # smooth RV data
	plt.legend(loc='lower right', numpoints = 1)

	plt.xlabel('JD - 2.44e6')
	plt.ylabel('RV (m/s)')

	plt.show()






