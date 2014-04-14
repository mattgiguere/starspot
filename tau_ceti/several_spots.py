import numpy as np
import random
from matplotlib import pyplot as plt

### Tau-Ceti fit to break signal by spots ###

data = np.load("TauCetiRVs.npy")

time = data[:,0]
rv = data[:,1]
rv_err = data[:,2]
smooth_rv = data[:,3]

# raw data
plt.plot(time, rv, 'o')

# smoothed data (method used?)
plt.plot(time, rv_smooth, 'o')

### break up 1: (16241, -4.93) to (16338, -0.006) ###
newdata = np.loadtxt("tau_ceti1.txt", delimiter=",", skiprows=1) # create new file
np.save("cutdata.npy",newdata) # save as .npy
newdata1 = np.load("cutdata.npy")

time1 = newdata1[:,0]
rv1 = newdata1[:,1]
rv_err1 = newdata1[:,2]
smooth_rv1 = newdata1[:,3]

plt.plot(time1, smooth_rv1, 'o') # excised data1

# slanted trig fit (by hand)

x = linspace(16220, 16350, 600)
y = 3*np.sin((2*math.pi)*(x+12)/32) + 0.027*x -439.7
plt.plot(x,y)

### break up 2: (16502.2, -4.51) to (16607.7, -2.98) ###
newnewdata = np.loadtxt("tau_ceti2.txt", delimiter=",", skiprows=10)
np.save("cutdata2.npy",newnewdata) # save as .npy
newdata2 = np.load("cutdata2.npy")

time2 = newdata2[:,0]
rv2 = newdata2[:,1]
rv_err2 = newdata2[:,2]
smooth_rv2 = newdata2[:,3]

plt.plot(time2, smooth_rv2, 'o') # excised data2






