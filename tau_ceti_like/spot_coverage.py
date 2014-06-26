# Written by Aida Behmard, 6/25/2014
# Computes spot coverage given photometric data

from __future__ import division

import numpy as np
import math
import matplotlib.pyplot as plt

from pylab import *
from numpy import *
from scipy import signal

# Load Data
star = np.loadtxt('noisy/4660971.txt')

t = star[:,1] 
y = star[:,2] # corrected PDCSAP_flux

# trial
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

plot(t, y, "k.")
y_av = running_average(y, 5)
plot(t, y_av, 'o', color = 'r')
xlim(0.0, 1600.0)
xlabel("BJD")
ylabel("Flux")
title("Running Average")
grid(True)
show()





