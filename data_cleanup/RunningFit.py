# Written by Aida Behmard, 6/6/2014
# Running average smoothes RV data 

from __future__ import division
from pylab import *
from numpy import *

import numpy as np
from scipy import signal

data = np.load('cutdata.npy') # example

def running_average(interval, window_size):
	# window_size: number of samples to consider
	# window is centered on each sample
	window = np.ones(int(window_size))/float(window_size) 
	return np.convolve(interval, window, 'same')

t = data[:,0]
y = data[:,1]

plot(t, y, "k.")
y_av = running_average(y, 20)
plot(t, y_av, 'o', color = 'r')
xlim(16241.718, 16336.539)
xlabel("Julian Days")
ylabel("RV (m/s)")
title("Tau Ceti: Running Average")
grid(True)
show()

# detrend 
y_av_flat = signal.detrend(y_av)

# Save the data to a CSV file
np.savetxt('clean_fit.txt', np.c_[t, y_av_flat, y])
print "File saved with filename: clean_fit.txt"
