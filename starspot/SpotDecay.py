# -*- coding: utf-8 -*-

# Written by Aida Behmard, 5/14/2014
# Program that adds time-varying component to starspot area
# Empirical expressions from sunspot data
# fracarea max ~0.000984 (3000 MSH), observed by Livadiotis & Moussas (2007)
# Only umbral area considered

import numpy as np
import math
import random

def spot_decay(time, fracarea):
    # Given initial fractional area (fracarea), compute spot dissolution

    # calculate decay rate D from Martínez et al. (1993)
    # D: MSH/day
    D = np.random.lognormal(1.75,math.sqrt(2),1)
    print "Decay Rate:", D

    initial_area = fracarea*(6.1*10**12) # solar surface area 
    print "Inital Area:", initial_area

    # pick exponential decay (A > 200 MSH) from Bumba (1963)
    if fracarea > 0.00009836:
        spot_area = initial_area*math.exp(-time/2)
        print "Exponential"

    # pick parabolic decay (A < 35 MSH) from Baumann & Solanki (2005)
    elif fracarea < 0.00001721 and time <= initial_area/D:
        spot_area = (math.sqrt(initial_area) - (D/math.sqrt(initial_area))*(time))**2 
        print "Parabolic"

    elif fracarea < 0.00001721 and time > initial_area/D:
        spot_area = 0
        print "Parabolic, time condition not met"

    # pick linear decay (35 MSH < A < 200 MSH) from Baumann & Solanki (2005)
    elif 0.00001721 < fracarea < 0.00009836 and time <= initial_area/D:
        spot_area = initial_area - D*time
        print "Linear"

    elif 0.00001721 < fracarea < 0.00009836 and time > initial_area/D:
        spot_area = 0
        print "Linear, time condition not met"

    print "Spot Area (km^2):", spot_area 
    fracarea = spot_area/(6.1*10**12) 
    print "fracarea:", fracarea

    if fracarea <= 0.0000001:
        return 0
    else:
        spot_decay(time, fracarea)
        print "new", fracarea 



        

