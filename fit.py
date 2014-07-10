# fit.py: RV curve fitting.
# pulls from FastOccluder.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from scipy.stats import linregress
from starspot import *

data = np.load('interesting_stars/tau_ceti/npy/cutdata.npy')

T = data[:,0] * 86400.
RV = data[:,3]

m, b, _, _, _ = linregress(T, RV)
RV -= m*T + b

def rv(p):
    inc, lat, phase, size, lat2, phase2, size2 = p
    star = RigidSphere(0.793 * 6.955e8, 34. * 86400., [0, math.cos(inc), math.sin(inc)])
    occ = FastOccluder(star, [star.spot(lat, phase, size), star.spot(lat2, phase2, size2)]) # add for multiple spots
    return get_rvs(occ, T)

# coarse search over parameter space to find a guess
def guess_fit():
    res = 12
    n = 0
    best_params = None
    best_err = None
    for inc in np.linspace(35, 35, res):
        for lat in np.linspace(55, 55, res):
            for phase in np.linspace(0, 0, res):
                for size in np.linspace(0, 0.01, res):
                    for lat2 in np.linspace(55, 55, res):
                        for phase2 in np.linspace(2/3, 2/3, res):
                            for size2 in np.linspace(0, 0.01, res):
                                n += 1
                                print "try %d/%d" % (n, res**4)
                                p = [inc, lat, phase, size, lat2, phase2, size2]
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

# Save the data to a CSV file
fit_rv = rv(bp) + m*T + b
true_rv = RV + m*T + b 

np.savetxt('rv_fit.txt', np.c_[T,fit_rv,true_rv])
print "File saved with filename: rv_fit.txt"
