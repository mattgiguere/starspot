# Written by Aida Behmard, 6/23/2014
# Outputs periodogram given time series Kepler transit data
# G8 dwarfs: 5200 < T < 5300, log(g) > 4.4, Kep_mag < 11.5

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle
from numpy import hstack
import heapq

# Load Data
star = np.loadtxt('running_av.txt') # from ewra.py

quarter_raw = star[:,0]
t_raw = star[:,1]
y_av = star[:,2]
y_raw = star[:,3] # corrected PDCSAP_FLUX (detrended, added back median)


# ---------- Exclude Outliers -------------------

# if fit is above raw value
good_1 = np.where((y_av > y_raw) & (y_av > 0) & (y_raw > 0))
diff_1 = y_av[good_1] - y_raw[good_1] 
t_1 = t_raw[good_1]

good_2 = np.where((y_av > y_raw) & (y_av > 0) & (y_raw < 0))
diff_2 = y_av[good_2] - y_raw[good_2]
t_2 = t_raw[good_2]

good_3 = np.where((y_av > y_raw) & (y_av < 0) & (y_raw < 0))
diff_3 = -(y_raw[good_3]) + y_av[good_3]
t_3 = t_raw[good_3]

# if fit is below raw value
good_4 = np.where((y_raw > y_av) & (y_av > 0) & (y_raw > 0))
diff_4 = y_raw[good_4] - y_av[good_4]
t_4 = t_raw[good_4]

good_5 = np.where((y_raw > y_av) & (y_raw > 0) & (y_av < 0))
diff_5 = y_raw[good_5] - y_av[good_5]
t_5 = t_raw[good_5]

good_6 = np.where((y_raw > y_av) & (y_raw < 0) & (y_av < 0))
diff_6 = -(y_av[good_6]) + y_raw[good_6]
t_6 = t_raw[good_6]

t = np.hstack((t_1, t_2, t_3, t_4, t_5, t_6))
diff = np.hstack((diff_1, diff_2, diff_3, diff_4, diff_5, diff_6))

print "total quantity:", len(diff) # check that correct values are considered
top = np.percentile(diff, 99.7) # 3-sigma cut-off
print "outlier cut-off:", top

plt.plot(t, diff, '.')
plt.title('Outliers')
plt.xlabel('Julian Days')
plt.ylabel('Flux Difference')

out = np.where(diff > top) # outlier condition
plt.plot(t[out], diff[out], 'ro')
plt.show()

# exclude NaNs 
keep = ~np.isnan(y_raw)
y_int = y_raw[keep]
t_int = t_raw[keep]

good = np.where(diff < top) 
y = y_int[good]
t = t_int[good]

# Save the data to a .txt file
np.savetxt('out_cut.txt', np.c_[t, y])
print "File saved with filename: out_cut.txt"


# ------------ Generate Periodogram -----------------------

# generates 1000 ang. frequencies 
nout = 1000.0
f = np.linspace(0.0001, 20.0, nout)

print "'periodogram(t, y, f)' for no outliers, 'periodogram(t_raw, y_raw, f)' for raw data"

def periodogram(time, flux, f):

    # computed periodogram is unnormalized
    # takes the value (A**2) * N/4
    # for a harmonic signal with amplitude A for sufficiently large N

    pgram = lombscargle(time, flux, f)

    plt.subplot(2, 1, 1)
    plt.plot(time, flux, '.')
    plt.xlabel('Time (MJD)')
    plt.ylabel('Flux')

    normval = t.shape[0]

    plt.subplot(2, 1, 2)
    power = np.sqrt(4*(pgram/normval))

    # plot normalized periodogram

    plt.plot(f, power)
    plt.xlabel('Ang. Frequency (MJD)')
    plt.ylabel('Power')

    plt.show()

    big_frequency = f[np.argmax(pgram)] # dominant ang. frequency
    big_power = power[np.argmax(pgram)] # dominant power
    print "dominant ang. frequency =", big_frequency
    print "domninant power =", big_power


