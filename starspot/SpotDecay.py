# -*- coding: utf-8 -*-

# Written by Aida Behmard, 5/14/2014
# Program that adds time-varying component to starspot area
# Empirical expressions from sunspot data
# fracarea max ~0.000984 (3000 MSH), observed by Livadiotis & Moussas (2007)
# Only umbral area considered

import numpy as np
import math
import random
import sys

def spot_decay(t, fracarea): # time = 1

    # Given initial fractional area (fracarea), compute spot dissolution
    # calculate decay rate D from Martínez et al. (1993)
    # D: km^2/day

    #sys.setrecursionlimit(50000)

    D_MSH = np.random.lognormal(1.75, math.sqrt(2), 1) # MSH/day 
    D = D_MSH*3*10**6
    print "Decay Rate:", D

    initial_area = fracarea*(6.1*10**12) # solar surface area 
    print "Inital Area (km^2):", initial_area

    # pick exponential decay (A > 200 MSH) from Bumba (1963)
    if fracarea > 0.00009836:
        spot_area = initial_area*math.exp(-t/2)
        print "Model: Exponential"

    # pick parabolic decay (A < 35 MSH) from Baumann & Solanki (2005)
    elif fracarea < 0.00001721 and t <= initial_area/D:
        spot_area = (math.sqrt(initial_area) - (D/math.sqrt(initial_area))*(t))**2 
        print "Model: Parabolic"

    elif fracarea < 0.00001721 and t > initial_area/D:
        spot_area = 0
        print "Model: Parabolic, time condition not met"

    # pick linear decay (35 MSH < A < 200 MSH) from Baumann & Solanki (2005)
    elif 0.00001721 < fracarea < 0.00009836 and t <= initial_area/D:
        spot_area = initial_area - D*t
        print "Model: Linear"

    elif 0.00001721 < fracarea < 0.00009836 and t > initial_area/D:
        spot_area = 0
        print "Model: Linear, time condition not met"

    print "Current Area (km^2):", spot_area 
    fracarea2 = spot_area/(6.1*10**12) 
    return fracarea2

    #if fracarea2 > 0.000000001:
        #spot_decay(t, fracarea2)

    #else:
        #print "Area = 0"

    # Save the data to a CSV file
    ## fit_rv = rv(bp) + m*T + b
    ## true_rv = RV + m*T + b 

    ## np.savetxt('spot_decay.txt', np.c_[T,fit_rv,true_rv])
    ## print "File saved with filename: rv_fit.txt"

    



        

