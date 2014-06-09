# Written by Aida Behmard, 6/9/2014
# Plots periodogram for Kepler time series data
# Interested in G8 dwarfs

import numpy as np
import math
from matplotlib import pyplot as plt 
from astroML.time_series import *
from astroML.plotting import setup_text_plots
setup_text_plots(fontsize = 8, usetex = True)

# Kepler data analysis
data = "wolf.npy"
t = data[:,0]
y = data[:,1]
dy = np.ones(297)
y_obs = np.random.normal(y, dy)

# Compute periodogram
period = 10 ** np.linspace(-1, 0, 10000)
omega = 2 * math.pi / period
PS = lomb_scargle(t, y_obs, dy, omega, generalized = True)

# get significance via bootstrap
D = lomb_scargle_bootstrap(y, y_obs, dy, omega, generalized = True,
	N_bootstraps = 1000, random_state = 0)

sig1, sig5 = np.percentile(D, [99,95])

# Plot the results
fig = plt.figure(figsize=(5, 3.75))
fig.subplots_adjust(left=0.1, right=0.9, hspace=0.25)

# First panel: the data
ax = fig.add_subplot(211)
ax.errorbar(t, y_obs, dy, fmt='.k', lw=1, ecolor='gray')
ax.set_xlabel('time (days)')
ax.set_ylabel('flux')
ax.set_xlim(-5, 105)

# Second panel: the periodogram & significance levels
ax1 = fig.add_subplot(212, xscale='log')
ax1.plot(period, PS, '-', c='black', lw=1, zorder=1)
ax1.plot([period[0], period[-1]], [sig1, sig1], ':', c='black')
ax1.plot([period[0], period[-1]], [sig5, sig5], ':', c='black')

ax1.annotate("", (0.3, 0.65), (0.3, 0.85), ha='center',
             arrowprops=dict(arrowstyle='->'))

ax1.set_xlim(period[0], period[-1])
ax1.set_ylim(-0.05, 0.85)

ax1.set_xlabel(r'period (days)')
ax1.set_ylabel('power')

# Twin axis: label BIC on the right side
ax2 = ax1.twinx()
ax2.set_ylim(tuple(lomb_scargle_BIC(ax1.get_ylim(), y_obs, dy)))
ax2.set_ylabel(r'$\Delta BIC$')

ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
ax1.xaxis.set_minor_formatter(plt.FormatStrFormatter('%.1f'))
ax1.xaxis.set_major_locator(plt.LogLocator(10))
ax1.xaxis.set_major_formatter(plt.FormatStrFormatter('%.3g'))

plt.show()



