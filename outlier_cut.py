# Written by Aida Behmard, 7/1/2014
# Excludes outliers from transit time series 

import numpy as np
import math
import matplotlib.pyplot as plt

from numpy import hstack

data = np.loadtxt('running_average.txt')

t = data[:,0]
y_av = data[:,1]
y = data[:,2]

print "type: 'cut_outliers(t, y, y_av)'"

def cut_outliers(t, y, y_av):

	# if fit is above raw value
	good_1 = np.where((y_av > y) & (y_av > 0) & (y > 0))
	diff_1 = y_av[good_1] - y[good_1] 
	t_1 = t[good_1]

	good_2 = np.where((y_av > y) & (y_av > 0) & (y < 0))
	diff_2 = y_av[good_2] - y[good_2]
	t_2 = t[good_2]

	good_3 = np.where((y_av > y) & (y_av < 0) & (y < 0))
	diff_3 = -(y[good_3]) + y_av[good_3]
	t_3 = t[good_3]

	# if fit is below raw value
	good_4 = np.where((y > y_av) & (y_av > 0) & (y > 0))
	diff_4 = y[good_4] - y_av[good_4]
	t_4 = t[good_4]

	good_5 = np.where((y > y_av) & (y > 0) & (y_av < 0))
	diff_5 = y[good_5] - y_av[good_5]
	t_5 = t[good_5]

	good_6 = np.where((y > y_av) & (y < 0) & (y_av < 0))
	diff_6 = -(y_av[good_6]) + y[good_6]
	t_6 = t[good_6]

	t = np.hstack((t_1, t_2, t_3, t_4, t_5, t_6))
	diff = np.hstack((diff_1, diff_2, diff_3, diff_4, diff_5, diff_6))

	plt.plot(t, diff, 'o')
	plt.show()

	# Save the data to a .txt file
	np.savetxt('outliers.txt', np.c_[t, diff])
	print "File saved with filename: outliers.txt"




