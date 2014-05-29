# fit.py: RV curve fitting.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from scipy.stats import linregress
from starspot import *

data = np.load('tau_ceti/cutdata.npy')

T = data[:,0] * 86400.
RV = data[:,3]

m, b, _, _, _ = linregress(T, RV)
RV -= m*T + b


def rv(p):
    inc, lat, phase, size = p
    star = RigidSphere(0.793 * 6.955e8, 34. * 86400., [0,math.cos(inc),math.sin(inc)])
    occ = FastOccluder(star, [star.spot(lat, phase, size)])
    return get_rvs(occ, T)

# coarse search over parameter space to find a guess
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
                    e = np.linalg.norm( r - RV )
                    if best_err == None or e < best_err:
                        best_params = p
                        best_err = e
    return best_params

# use nonlinear optimization to refine fit
def refine_fit(guess):
    opt = leastsq(rv, guess)
    return opt

bp = guess_fit()
print bp

plt.clf()
plt.scatter(T, RV + m*T + b)
plt.plot(T, rv(bp) + m*T + b, label='guess')
plt.legend()
plt.show()
