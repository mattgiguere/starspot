# Written by Aida Behmard, 6/25/2014
# Computes spot coverage given photometric data

import numpy as np
import math
import matplotlib.pyplot as plt

from numpy import percentile

# Load Data
star = np.loadtxt('someting_something_tau_ceti')

t = star[:,0] 
y = star[:,3] # corrected PDCSAP_flux

plt.subplot(2, 1, 1)
plt.plot(t, y, '.', label = 'raw')
plt.legend(loc='upper right', numpoints = 1)

top = np.percentile(y, 99.9)
bottom = np.percentile(y, 0.1)

keep = np.where(y < top)
y = y[keep]
t = t[keep]

and_keep = np.where(bottom < y)
y = y[and_keep]
t = t[and_keep]

plt.subplot(2, 1, 2)
plt.plot(t, y, '.', label = 'clean')
plt.legend(loc='upper right', numpoints = 1)

plt.show()

print "top cut-off:", top
print "bottom cut-off:", bottom

# ran on:
# 4831454
# 10006542
# 3437637
# 3956527
# 4457351
# 5390769
# 5512283
# 6848299
# 7970740
# 9468214
# 9760257
# 9996021
# 10186796







