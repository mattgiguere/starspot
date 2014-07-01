# Written by Aida Behmard, 6/26/2014
# Cuts out short cadence data

import numpy as np
import math
import matplotlib.pyplot as plt

star = np.loadtxt('flat/10186796.txt')

quarter = star[:,0]
t = star[:,1]
flux = star[:,2]

keep = np.where(quarter <= 17)

quarter = quarter[keep]
flux = flux[keep]
t = t[keep]

np.savetxt('fix.txt', np.c_[quarter, t, flux])
print "File saved with filename: fix.txt"


