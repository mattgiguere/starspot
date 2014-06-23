# Written by Aida Behmard, 6/10/2014
# Outputs periodogram given time series Kepler transit data
# G8 dwarfs: 5200 < T < 5300, log(g) > 4.4, Kep_mag < 10

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle

#------------------------------------------------------------
# Load Data
star = np.loadtxt('kepler_data/kepfinal.txt')

# generates 10000 ang. frequencies between 16240 and 16340
nout = 1000.0
f = np.linspace(1.0, 10.0, nout)

t = star[:,0] 
y = star[:,3] # corrected flux

# exclude NaNs in data
keep = ~np.isnan(y)
y = y[keep]
t = t[keep]
y -= np.mean(y)

print "type 'periodogram(t, y, f)'"

def periodogram(time, flux, f):

    # computed periodogram is unnormalized
	# takes the value (A**2) * N/4
	# for a harmonic signal with amplitude A for sufficiently large N

    pgram = lombscargle(time, flux, f)

    plt.subplot(2, 1, 1)
    plt.plot(time, flux, '.', label = 'Time Series')
    plt.legend(loc='lower right', numpoints = 1)
    plt.xlabel('Time (MJD)')
    plt.ylabel('Flux')

    normval = t.shape[0]

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