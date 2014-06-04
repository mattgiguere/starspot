# Written by Aida Behmard, 6/4/2014
# Smoothes raw RV data 
# "wiener(t,y,y_smooth)"

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import wiener 
from pylab import *

data = np.load('tau_ceti/cutdata.npy') # example

t = data[:,0]
y = data[:,1]
y_wiener = wiener(data[:,1])
y_smooth = data[:,3]

def wiener(time, rv, rv_smooth):
	# Using Wiener filter
	plt.figure(1)
	plt.subplot(211)
	plt.plot(t, y, 'o', color = 'b', label = 'Raw')
	plt.plot(t, y, color = 'b') # raw RV data

	plt.plot(t, y_wiener, 'o', color = 'r', label = 'Wiener') # smooth RV data
	plt.legend(loc='lower right', numpoints = 1)

	plt.title('Tau Ceti: Wiener Filter')
	plt.xlabel('JD - 2.44e6')
	plt.ylabel('RV (m/s)')

    # Using default smooth data
	plt.subplot(212)
	plt.plot(t, y, 'o', color = 'b', label = 'Raw')
	plt.plot(t, y, color = 'b') # raw RV data

	plt.plot(t, y_smooth, 'o', color = 'r', label = 'Default Smooth') # smooth RV data
	plt.legend(loc='lower right', numpoints = 1)

	plt.xlabel('JD - 2.44e6')
	plt.ylabel('RV (m/s)')

	plt.show()




