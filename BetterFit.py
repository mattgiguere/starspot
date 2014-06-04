# Written by Aida Behmard, 6/3/2014
# Rigorous replacement for fit.py
# Employes max entropy model (MEM)

# Saves data to a CSV

import numpy as np
import matplotlib.pyplot as plt
from starspot import *

from scipy.optimize import leastsq
from scipy.stats import linregress
from scipy import maxentropy

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