# Written by Aida Behmard, 6/10/2014
# Outputs periodogram give time series transit data
# G8 dwarfs: 5000 < T < 50001, log(g) > 4.4

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle
from numpy import float64
from numpy import isnan

#------------------------------------------------------------
# Load Data
star = pyfits.open('kepler_data/mou.fits')
tbdata = star[1].data

# generates 10000 ang. frequencies between 16240 and 16340
nout = 1000.0
f = np.linspace(1.0, 2000.0, nout)

t = tbdata.field(0) 
y = tbdata.field(7) # corrected flux

print "type 'periodogram(t, y, f)'"

def periodogram(time, flux, f):

	newt = t.byteswap().newbyteorder()
	newy = y.byteswap().newbyteorder()

	# computed periodogram is unnormalized
	# takes the value (A**2) * N/4
	# for a harmonic signal with amplitude A for sufficiently large N

	keep = ~np.isnan(newy)
	newy = newy[keep]
	newt = newt[keep]
	newy -= np.mean(newy)

	pgram = lombscargle(newt.astype('float64'), newy.astype('float64'), f)

	plt.subplot(2, 1, 1)
	plt.plot(newt.astype('float64'), newy.astype('float64'), 'b+', label = 'Time Series')
	plt.legend(loc='lower right', numpoints = 1)
	plt.xlabel('Time')
	plt.ylabel('Flux')

	normval = newt.shape[0]

	plt.subplot(2, 1, 2)

	print f, pgram

	# plot normalized periodogram
	plt.plot(f, np.sqrt(4*pgram/normval), label = 'Periodogram')
	plt.legend(loc='upper right', numpoints = 1)
	plt.xlabel('Frequency')   
	plt.ylabel('Power')

	plt.show()

	big_freq = f[np.argmax(pgram)]
	print "dominant frequency =", big_freq
