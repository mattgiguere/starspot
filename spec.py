# spec.py: spectrum demo for starspot library.

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

period = 20*86400
sun = RigidSphere(6.955e8, period, [0,1,2])
spots = [sun.spot(45,0,10e7)]
rt = Raytracer(sun, 50, spots)

# simulate RV measurement with Voigt spectra at a time
def slow_rv(t):
    mask = rt.trace(t)
    rgb = rt.render(mask)

    x = np.linspace(0,1,1000)
    base = physics.voigt(x, 1, 0.5, 0.1, 0)

    ret = np.zeros( base.shape )
    for rv, m in zip(rt.radvels, mask):
        ret += m * physics.voigt(x + rv/10000.0, 1, 0.5, 0.1, 0)
    ret /= mask.sum()

    return np.average(x, weights=ret)

# simulate RV measurement with weighted average
def fast_rv(t):
    mask = rt.trace(t)
    return rt.mean_radvel(mask)

# demo: render evolution and curve
def render_one():
    renders = 5
    samples = 60
    T = np.linspace(0,2*period,samples)
    rv = np.zeros(samples)

    for i,t in enumerate(T):
        print "trace %d/%d (t=%f)" % (i+1, len(T), t)
        rv[i] = fast_rv(t)


    plt.clf()
    plt.subplot2grid((2,renders),(0,0), colspan=5)
    plt.plot(T,rv)

    for i in range(renders):
        plt.subplot2grid((2,renders),(1,i))
        print "render %d/%d (t=%f)" % (i+1, renders, t)
        t = 0.2*period*i/renders
        rgb = rt.render( rt.trace(t) )
        plt.axis('off')
        plt.imshow(rgb, interpolation='nearest', origin='lower')

    plt.show()
