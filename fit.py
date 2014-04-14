# fit.py: RV curve fitting.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from starspot import *

data = np.load('tau_ceti/cutdata.npy')

T = data[:,0] * 86400.
RV = data[:,3]

m, b, _, _, _ = linregress(T, RV)
RV -= m*T + b

def rv(inc, lat, phase, size):
    star = RigidSphere(0.793 * 6.955e8, 34. * 86400., [0,math.cos(inc),math.sin(inc)])
    occ = FastOccluder(star, [star.spot(lat, phase, size)])
    return get_rvs(occ, T)

res = 10
n = 0
best_params = None
best_err = None
for inc in np.linspace(-60, 60, res):
    for lat in np.linspace(-90, 90, res):
        for phase in np.linspace(0, 1, res):
            for size in np.linspace(0, 0.01, res):
                n += 1
                print "try %d/%d" % (n, res**4)
                r = rv(inc, lat, phase, size)
                e = np.linalg.norm(r - RV)
                if best_err == None or e < best_err:
                    best_params = [inc, lat, phase, size]
                    best_err = e

print best_params

plt.clf()
plt.scatter(T, RV)
plt.plot(T, rv(*best_params))
plt.show()
