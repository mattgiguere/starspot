# Written by Aida Behmard, 6/23/2014
# Outputs periodogram given time series Kepler transit data
# G8 dwarfs: 5200 < T < 5300, log(g) > 4.4, Kep_mag < 10

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle

#------------------------------------------------------------
# Load Data
star = np.loadtxt('tau_ceti_like/noisy/11924268.txt')

# generates 10000 ang. frequencies between 16240 and 16340
nout = 1000.0
f = np.linspace(0.03, 10.0, nout)

t_raw = star[:,1] 
y_raw = star[:,2] # corrected PDCSAP_flux

# exclude NaNs in data
keep = ~np.isnan(y_raw)
y = y_raw[keep]
t = t_raw[keep]
y -= np.median(y)

print "type 'periodogram(t, y, f)'"

def periodogram(time, flux, f):

    # computed periodogram is unnormalized
	# takes the value (A**2) * N/4
	# for a harmonic signal with amplitude A for sufficiently large N

    pgram = lombscargle(time, flux, f)

    plt.subplot(2, 1, 1)
    plt.plot(time, flux, '.', label = 'Time Series')
    plt.legend(loc='upper right', numpoints = 1)
    plt.xlabel('Time (MJD)')
    plt.ylabel('Flux')

    normval = t.shape[0]

    plt.subplot(2, 1, 2)

    print f, pgram
    period = 2*math.pi / f

    # plot normalized periodogram
    plt.plot(period, np.sqrt(4*pgram/normval), label = 'Periodogram')
    plt.legend(loc='upper right', numpoints = 1)
    plt.xlabel('Period (MJD)')
    plt.ylabel('Power')

    plt.show()

    big_period = period[np.argmax(pgram)]
    print "dominant period =", big_period

   