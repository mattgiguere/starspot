# Written by Aida Behmard, 6/30/2014
# Computes exponential weighted running average 
# Good for unevenly sampled time series

import matplotlib.pyplot as plt
import numpy as np

from scipy import signal
import pandas as pd

data = np.loadtxt('tau_ceti_like/noisy_data/5042255.txt')

quarter = data[:,0]
t = data[:,1]
y_raw = data[:,2]

end = max(quarter)

keep = np.where(quarter == 8)

quarter = quarter[keep]
y = y_raw[keep]
t = t[keep]

# detrend
# works if quarter offsets are corrected 
flux = signal.detrend(y) 
plt.plot(t, flux, 'ro')

flux_av = pd.stats.moments.ewma(flux, span = 5) # smaller span, sharper decay

plt.plot(t, flux_av)
plt.xlim(0, 1600)
plt.xlabel("Julian Days")
plt.ylabel("Flux")
plt.title("Exponentially Weighted Running Average")

plt.show()

# Save the data to a .txt file
np.savetxt('running_av.txt', np.c_[quarter, t, flux_av, flux])
print "File saved with filename: running_av.txt"
