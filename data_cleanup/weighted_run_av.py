# Written by Aida Behmard, 6/30/2014
# Computes exponential weighted running average 
# Good for unevenly sampled time series

import matplotlib.pyplot as plt
import numpy as np

from scipy import signal
import pandas as pd

data = np.loadtxt('tau_ceti_like/noisy/4660971.txt') 

t = data[:,1]
y_raw = data[:,2]

# detrend
y = signal.detrend(y_raw)

plt.plot(t, y, 'ro')

y_av = pd.stats.moments.ewma(y, span = 20)

plt.plot(t, y_av)
plt.xlim(400, 750)
plt.xlabel("Julian Days")
plt.ylabel("RV (m/s)")
plt.title("Exponentially Weighted Running Average")

plt.show()

# Save the data to a CSV file
np.savetxt('running_average.txt', np.c_[t, y_av, y])
print "File saved with filename: running_average.txt"

