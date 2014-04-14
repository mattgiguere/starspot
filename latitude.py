# latitude.py: animate the effect of latitude on the RV curve

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

samples = 100
frames = 100
period = 20*86400
T = np.linspace(0, 2*period, samples)
L = np.linspace(-90, 90, frames)

# render curve at a given latitude
def render_lat(lat):
    print "rendering latitude %f" % lat
    sun = RigidSphere(6.955e8, period, [0,1,1])
    spots = [sun.spot(lat,0.5,0.01)]
    rt = Raytracer(sun, 100, spots)

    rv = np.zeros(samples)
    for k,t in enumerate(T):
        print "trace %d/%d (t=%f)" % (k+1, len(T), t)
        rv[k] = rt.rv(t)

    return rv

for i,lat in enumerate(L):
    rv = render_lat(lat)
    plt.cla()
    plt.xlim(0,2*period/86400.)
    plt.ylim(-30,30)
    plt.xlabel('JD')
    plt.ylabel('RV (m/s)')
    plt.plot(T/86400.,rv)
    np.save('renders/latitude/rvdata/rv%d.npy' % i, rv)
    plt.savefig('renders/latitude/frames/frame%d.png' % i)
