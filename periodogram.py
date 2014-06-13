# Written by Aida Behmard, 6/10/2014
# Outputs periodogram give time series transit data
# G8 dwarfs: 5200 < T < 5300, log(g) > 4.4, Kep_mag < 10

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle
from numpy import float64
from numpy import isnan

#------------------------------------------------------------
# Load Data
star = pyfits.open('kepler_data/kplr007970740-2013131215648_llc.fits')
tbdata = star[1].data

# generates 10000 ang. frequencies between 16240 and 16340
nout = 1000.0
f = np.linspace(1.0, 8.0, nout)

t = tbdata.field(0) 
y = tbdata.field(7) # corrected flux

print "type 'periodogram(t, y, f)'"

def periodogram(time, flux, f):
 
    # endian conversion
	newt = t.byteswap().newbyteorder()
	newy = y.byteswap().newbyteorder()

    # exclude NaNs in data
	keep = ~np.isnan(newy)
	newy = newy[keep]
	newt = newt[keep]
	newy -= np.mean(newy)

    # computed periodogram is unnormalized
	# takes the value (A**2) * N/4
	# for a harmonic signal with amplitude A for sufficiently large N
	pgram = lombscargle(newt.astype('float64'), newy.astype('float64'), f)

	plt.subplot(2, 1, 1)
	plt.plot(newt.astype('float64'), newy.astype('float64'), '.', label = 'Time Series')
	plt.legend(loc='lower right', numpoints = 1)
	plt.xlabel('Time (MJD)')
	plt.ylabel('Flux')

	normval = newt.shape[0]

	plt.subplot(2, 1, 2)

	print f, pgram
	period = 2*math.pi / f

	# plot normalized periodogram
	plt.plot(period, np.sqrt(4*pgram/normval), label = 'Periodogram')
	plt.legend(loc='lower right', numpoints = 1)
	plt.xlabel('Period (MJD)')   
	plt.ylabel('Power')

	plt.show()

	big_period = period[np.argmax(pgram)]
	print "dominant period =", big_period
