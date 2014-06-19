# trace_anim.py: animate a transit

import numpy as np
from starspot import *
from starspot.geometry import inclined_axis

samples = 600
res = 200
frames = 100
period = 20*86400
lat = 30

sun = RigidSphere(6.955e8, period, [0,1,1])
spots = [sun.spot(lat,0.5,0.003)]
occ = FastOccluder(sun, spots)
rt = Raytracer(sun, spots, res)

T = np.linspace(0, period, samples)
Tr = np.linspace(0, period, frames)

rv = get_rvs(occ, T)
rvr = get_rvs(occ, Tr)
plt.clf()

def tr(ind):
    print "rendering frame %d/%d" % (ind+1, len(Tr))

    mask = rt.trace(Tr[ind])

    # trace
    plt.subplot2grid((2,2),(1,0),colspan=2)

    plt.cla()
    plt.xlim(0,period/86400.)
    plt.ylim(-15,15)

    plt.xlabel('JD')
    plt.ylabel('Apparent RV (m/s)')
    plt.plot(T/86400.,rv)

    plt.scatter([Tr[ind]/86400.],[rvr[ind]])

    # profile
    ax = plt.subplot2grid((2,2),(0,1))
    plt.cla()

    ax.set_yticks([])
    plt.xlabel('RV (m/s)')
    plt.ylabel('Relative Intensity')
    plt.locator_params(axis = 'x', nbins = 4)

    rvu = np.zeros(200)
    mu = np.zeros(200)
    for y,x,vel,atten in izip(rt.pixels[0], rt.pixels[1], rt.radvels, mask):
        rvu[y] = vel
        mu[y] += atten
    rvu[0] = 2*rvu[1] - rvu[2]
    rvu[-1] = 2*rvu[-2] - rvu[-3]
    plt.ylim(0, max(mu)*1.1)

    plt.plot(rvu,mu)

    plt.axvline(0, color='grey')
    plt.axvline(rvr[ind], color='red')

    # pic
    ax = plt.subplot2grid((2,2),(0,0), aspect='equal')
    plt.cla()
    ax.set_xticks([])
    ax.set_yticks([])

    pad=20
    plt.xlim(-pad,res+pad)
    plt.ylim(-pad,res+pad)

    rgb = rt.render(mask, soften_scale=2.)
    plt.imshow(rgb, origin='lower')

    # plt.show()

for i in range(len(Tr)):
    tr(i)
    plt.savefig('build/trace_anim/frame%03d.png' % i)
