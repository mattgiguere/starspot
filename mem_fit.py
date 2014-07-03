# Written by Aida Behmard, 6/3/2014
# Replacement for fit.py
# Achieves precisions of 1 m/s
# Employes max entropy model (MEM)

# Saves data to a CSV

import numpy as np
import matplotlib.pyplot as plt
from starspot import *

from scipy.optimize import leastsq
from scipy.stats import linregress
# from scipy import maxentropy

data = np.load('tau_ceti/npy/cutdata.npy')

T = data[:,0] * 86400.
RV = data[:,3]

# somehow picks nice values for m and b?
m, b, _, _, _ = linregress(T, RV)
RV -= m*T + b

# matches raw data to simulated star?
def rv(p):
    inc, lat, phase, size = p
    star = RigidSphere(0.793 * 6.955e8, 34. * 86400., [0,math.cos(inc),math.sin(inc)])
    occ = FastOccluder(star, [star.spot(lat, phase, size)])
    return get_rvs(occ, T)

# coarse search over parameter space to find a guess
# let's try chi-squared ~1 m/s
def guess_fit():
    res = 12
    n = 0
    best_params = None
    best_err = None
    for inc in np.linspace(0, 90, res):
        for lat in np.linspace(-inc, 90, res):
            for phase in np.linspace(0, 1, res):
                for size in np.linspace(0, 0.01, res):
                    n += 1
                    print "try %d/%d" % (n, res**4)
                    p = [inc, lat, phase, size]
                    r = rv(p)
                    e = np.linalg.norm( r - RV ) # picks one particular simulation setup?
                    if best_err == None or e < best_err:
                        best_params = p
                        best_err = e
    return best_params

# use nonlinear optimization to refine fit
def chisquared_fit(guess):
    opt = sum( math.sqrt((rv - guess)**2) / data[:,2]) 
    return opt

bp = guess_fit()
print bp

plt.clf()
plt.scatter(T, RV + m*T + b)
plt.plot(T, rv(bp) + m*T + b, label='guess')
plt.legend()
plt.show()

# Save the data to a CSV file
fit_rv = rv(bp) + m*T + b
true_rv = RV + m*T + b 

np.savetxt('rv_fit.txt', np.c_[T,fit_rv,true_rv])
print "File saved with filename: rv_fit.txt"