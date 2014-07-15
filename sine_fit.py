# Written by Aida Behmard, 7/14/2014
# Fits a sine function using FFT 
# Applied to Kepler photometric data

import numpy as np
import scipy.optimize as optimize
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

data = np.loadtxt('out_cut.txt') 

t = data[:,0]
flux = data[:,1]
N = len(t)

pi = np.pi
plt.figure(figsize = (15, 5))

def mysine(t, a1, a2, a3):
    return a1 * np.sin(a2 * t + a3)

yhat = fftpack.rfft(flux)
idx = (yhat**2).argmax()
freqs = fftpack.rfftfreq(N, d = (t[1]-t[0])/(2*pi))
frequency = freqs[idx]

amplitude = flux.max()
guess = [amplitude, 0.76, 0.]
print "guessed amplitude & ang. frequency:", guess
(amplitude, frequency, phase), pcov = optimize.curve_fit(
    mysine, t, flux, guess)

period = 2*pi/frequency
print "amplitude & ang. frequency & phase:", amplitude, frequency, phase

xx = t
yy = mysine(xx, amplitude, frequency, phase)
# plot the real data
plt.plot(t, flux, 'r', label = 'Real Values')
plt.plot(xx, yy , label = 'fit')
plt.legend(shadow = True, fancybox = True)
plt.show()

