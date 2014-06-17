# Written by Aida Behmard, 6/6/2014
# Running average smoothes RV data 

from __future__ import division
from pylab import *
from numpy import *
import numpy as np

data = np.load('tau_ceti/cutdata.npy') # example

def running_average(interval, window_size):
	window = np.ones(int(window_size))/float(window_size)
	return np.convolve(interval, window, 'same')

t = data[:,0]
y = data[:,1]

plot(t, y, "k.")
y_av = running_average(y, 10)
plot(t, y_av, 'o', color = 'r')
xlim(16241.718, 16336.539)
xlabel("Julian Days")
ylabel("RV (m/s)")
title("Tau Ceti: Running Average")
grid(True)
show()
