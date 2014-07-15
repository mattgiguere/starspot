import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
from scipy.stats import linregress
from starspot import *

data = np.load('interesting_stars/tau_ceti/npy/cutdata.npy')

T = data[:,0] * 86400.
RV = data[:,3]

inc = 35.

m, b, _, _, _ = linregress(T, RV)
RV -= m*T + b

def rv(p):
    t_eq, t_pol, lat, phase, size = p
    inc_radians = inc * np.pi/180.;
    star = FluidSphere(0.793 * 6.955e8, t_eq, t_pol, [0,math.cos(inc),math.sin(inc)])
    occ = FastOccluder(star, [star.spot(lat, phase, size)])
    return get_rvs(occ, T)

# coarse search over parameter space to find a guess
def guess_fit():
    res = [5,5,12,12,12] # separate resolutions for each parameter
    ntries = reduce(lambda x,y: x*y, res)

    n = 0
    best_params = None
    best_err = None
    for t_eq in 86400. * np.linspace(20, 30, res[0]): # equatorial period: 20 to 30 days
        for t_pol in 86400. * np.linspace(t_eq, 30, res[1]): # polar period: t_eq to 30 days
            for lat in np.linspace(-inc, 90, res[2]):
                for phase in np.linspace(0, 1, res[3]):
                    for size in np.linspace(0, 0.01, res[4]):
                        n += 1
                        print "try %d/%d" % (n, ntries)
                        p = [t_eq, t_pol, lat, phase, size]
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
