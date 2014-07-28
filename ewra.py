# Written by Aida Behmard, 6/30/2014
# Computes exponential weighted running average 
# Good for unevenly sampled time series

import matplotlib.pyplot as plt
import numpy as np

from scipy import signal
import pandas as pd

data = np.loadtxt('tau_ceti_like/noisy_data/4732422.txt') 

t = data[:,1]
y_raw = data[:,2]

# detrend
# works if quarter offsets are corrected 
y = signal.detrend(y_raw) 
plt.plot(t, y, 'ro')

y_av = pd.stats.moments.ewma(y, span = 5) # smaller span, sharper decay

plt.plot(t, y_av)
plt.xlim(850, 1600)
plt.xlabel("Julian Days")
plt.ylabel("Flux")
plt.title("Exponentially Weighted Running Average")

plt.show()

# Save the data to a .txt file
np.savetxt('running_average.txt', np.c_[t, y_av, y])
print "File saved with filename: running_average.txt"
