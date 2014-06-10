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

# generates 10000 ang. frequencies between 16240 and 16340
nout = 10000
f = np.linspace(16240, 16340, nout)

def periodogram(data, f):
	t = data[:,0]
	y = data[:,1] # flux
	dy = data[:,2]

	# computed periodogram is unnormalized
	# takes the value (A**2) * N/4
	# for a harmonic signal with amplitude A for sufficiently large N

	pgram = lombscargle(t, y, f)

	plt.subplot(2, 1, 1)
	plt.plot(t, y, 'b+', label = 'Time Series')
	plt.legend(loc='lower right', numpoints = 1)
	plt.xlabel('Time')
	plt.ylabel('Flux')

	normval = t.shape[0]

	plt.subplot(2, 1, 2)

	# plot normalized periodogram
	plt.plot(f, np.sqrt(4*(pgram/normval)), label = 'Periodogram')
	plt.legend(loc='upper right', numpoints = 1)
	plt.xlabel('Frequency')   
	plt.ylabel('Power')

	plt.show()

	big_freq = f[np.argmax(pgram)]
	print "dominant frequency =", big_freq
