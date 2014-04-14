# specgrid.py: RV demo, rendering family of curves

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

# demo: render a grid of curves
def render_grid():
    samples = 40
    ax = [ inclined_axis(theta) for theta in range(0,90,15) ]
    lat = [ theta for theta in range(0,90,15) ]
    plax = None
    for i,a in enumerate(ax):
        for j,l in enumerate(lat):
            print "rendering time series (%d,%d)" % (i+1,j+1)
            if plax:
                plt.subplot2grid( (len(ax), len(lat)), (i, j), sharey=plax )
            else:
                plax = plt.subplot2grid( (len(ax), len(lat)), (i, j) )

            period = 20*86400
            sun = RigidSphere(6.955e8, period, a)
            spots = [sun.spot(l,0,0.01)]
            rt = Raytracer(sun, 40, spots)

            T = np.linspace(0, 2*period, samples)
            rv = np.zeros(samples)
            for k,t in enumerate(T):
                print "trace %d/%d (t=%f)" % (k+1, len(T), t)
                rv[k] = rt.mean_radvel( rt.trace(t) )

            plt.plot(T, rv)

plt.clf()
render_grid()
plt.show()