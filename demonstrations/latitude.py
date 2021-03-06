# latitude.py: animate the effect of latitude on the RV curve

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

samples = 600
frames = 100
period = 20*86400
T = np.linspace(0, 2*period, samples)
L = np.linspace(-45, 90, frames)

# render curve at a given latitude
def render_lat(lat):
    print "rendering latitude %f" % lat
    sun = RigidSphere(6.955e8, period, [0,1,1])
    spots = [sun.spot(lat,0.5,0.001)]
    occ = FastOccluder(sun, spots)
    return get_rvs(occ, T)

# draw a picture
def pic(lat):
    print "rendering latitude %f" % lat
    sun = RigidSphere(6.955e8, period, [0,1,1])
    spots = [sun.spot(lat,0,0.001)]
    rt = Raytracer(sun, spots, 100)
    rgb = rt.render(rt.trace(0))
    plt.axis('off')
    plt.imshow(rgb, interpolation='nearest', origin='lower')

def time_benchmark():
    for i,lat in enumerate(L):
        rv = render_lat(lat)

for i,lat in enumerate(L):
    # rv = render_lat(lat)
    plt.cla()
    # plt.xlim(0,2*period/86400.)
    # plt.ylim(-10,10)
    # plt.xlabel('JD')
    # plt.ylabel('RV (m/s)')
    # plt.plot(T/86400.,rv)
    # np.save('build/latitude/rvdata/rv%d.npy' % i, rv)
    pic(lat)
    plt.savefig('build/latitude/renders/frame%03d.png' % i)
