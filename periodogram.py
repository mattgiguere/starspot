# Written by Aida Behmard, 6/10/2014
# Outputs periodogram give time series transit data
# G8 dwarfs: 5000 < T < 50001, log(g) > 4.4

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import lombscargle

#------------------------------------------------------------
# Load Data
data = np.load('tau_ceti/cutdata.npy')

nout = 100000
f = np.linspace(0.01, 10, nout)
print "freqs", f

def periodogram(data, f):
	t = data[:,0]
	y = data[:,1] # flux
	dy = data[:,2]

	pgram = lombscargle(t, y, f)

	plt.subplot(2, 1, 1)
	plt.plot(t, y, 'b+', label = 'Time Series')
	plt.legend(loc='lower right', numpoints = 1)
	plt.xlabel('Time')
	plt.ylabel('Flux')

	normval = t.shape[0]

	plt.subplot(2, 1, 2)
	plt.plot(f, np.sqrt(4*(pgram/normval)), label = 'Periodogram')
	plt.legend(loc='upper right', numpoints = 1)
	plt.xlabel('Frequency')
	plt.ylabel('Power')

	plt.show()

	big_period = 2*math.pi / f[np.argmax(pgram)]
	print "dominant period", big_period
