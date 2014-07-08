# Written by Aida Behmard, 6/23/2014
# Outputs periodogram given time series Kepler transit data
# G8 dwarfs: 5200 < T < 5300, log(g) > 4.4, Kep_mag < 11.5

import numpy as np
import math
import pyfits
import matplotlib.pyplot as plt

from scipy.signal import lombscargle
from numpy import hstack

# Load Data
star = np.loadtxt('running_average.txt') # from ewra.py

t_raw = star[:,0]
y_av = star[:,1]
y_raw = star[:,2] # corrected PDCSAP_FLUX (detrended, added back median)


# ---------- Exclude Outliers -------------------

# if fit is above raw value
good_1 = np.where(y_av > y_raw)
diff_1 = y_av[good_1] - y_raw[good_1] 
t_1 = t_raw[good_1]
sigma_1 = y_raw[good_1] - np.median(y_raw[good_1])

# if fit is below raw value
good_2 = np.where((y_raw > y_av))
diff_2 = y_raw[good_2] - y_av[good_2]
t_2 = t_raw[good_2]
sigma_2 = y_raw[good_2] - np.median(y_raw[good_2])

t = np.hstack((t_1, t_2))
diff = np.hstack((diff_1, diff_2))
sigma = np.hstack((sigma_1, sigma_2))

print "total quantity:", len(diff) # check that correct values are considered
top = np.percentile(diff, 99.7) # 3-sigma cut-off
print "outlier cut-off:", top

out = np.where(diff > 145.084166338) # outlier condition
y_not = y_raw[out]
t_not = t_raw[out]
y_main = list(set(y_raw) - set(y_raw[out])) # subtract outliers
t_main = list(set(t_raw) - set(t_raw[out]))

y_keep = np.asarray(y_main) # convert list to array
t_keep = np.asarray(t_main)

# compute standard devations
plt.plot(sigma, diff, 'o')
plt.xlabel('sigma')
plt.ylabel('flux difference')
plt.title('5042255')
plt.show()