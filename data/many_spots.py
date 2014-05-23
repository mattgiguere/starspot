import numpy as np
import random
from matplotlib import pyplot as plt

### 1. Tau-Ceti fit to break signal by spots ###

data = np.load("TauCetiRVs.npy")

time = data[:,0]
rv = data[:,1]
rv_err = data[:,2]
smooth_rv = data[:,3]

# raw data
plt.plot(time, rv, 'o')

# smoothed data (method used?)
plt.plot(time, smooth_rv, 'o')

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

x = np.linspace(16220, 16350, 600)
y = 2.146*np.sin((2*math.pi)*(x+13)/32) + 0.027*x -439.9
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

### 2. HD166435 fit ###

newstar = np.loadtxt("HD166435_rvs.txt", delimiter=",", skiprows=1) # load data
np.save("HD166435.npy",newstar) # save as .npy
hd166435 = np.load("HD166435.npy")

time3 = hd166435[:,0]
rv3 = hd166435[:,1]

plt.plot(time3, rv3, 'o') 

### break up HD166435 for a closer look: (50858.703 , -14.502) to (50973.5709 , -14.397)

newstarcut = np.loadtxt("HD166435_cut.txt", delimiter=",", skiprows=1)
np.save("HD166435_cut.npy", newstarcut)
hd166435_cut = np.load("HD166435_cut.npy")

time4 = hd166435_cut[:,0]
rv4 = hd166435_cut[:,1]

plt.plot(time4, rv4, 'o')
x = np.linspace(50850, 50980, 600)
y = 0.083*np.sin((0.2518*math.pi)*(x-10)/3.785)-0.0003215*x+1.874

plt.plot(x,y)

### 3. Epsilon Eridani fit ###

e_star = np.loadtxt("epseri.txt", delimiter=",", skiprows=1)
np.save("eps_eri.npy", e_star)
eps_eri = np.load("eps_eri.npy")

time5 = eps_eri[:,0]
rv5 = eps_eri[:,1]

### break up 1: (16115.918, -24.4558) to (16378.493, 11.8805) ###

e_star1 = np.loadtxt("epseri_fit1.txt", delimiter=",", skiprows=1)
np.save("epseri_cut1", e_star1)
epseri_cut1 = np.load("epseri_cut1.npy")

time6 = epseri_cut1[:,0]
rv6 = epseri_cut1[:,1]

### break up 2: (16571.681, 15.2568) to (16646.731, 3.47041) ###

e_star2 = np.loadtxt("epseri_fit2.txt", delimiter=",", skiprows=1)
np.save("epseri_cut2", e_star2)
epseri_cut2 = np.load("epseri_cut2.npy")

time7 = epseri_cut2[:,0]
rv7 = epseri_cut2[:,1]

