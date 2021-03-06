# -*- coding: utf-8 -*-

# Written by Aida Behmard, 5/14/2014
# Program that adds time-varying component to starspot area
# Empirical expressions from sunspot data
# fracarea max ~0.000984 (3000 MSH), observed by Livadiotis & Moussas (2007)
# Only umbral area considered

import numpy as np
import math

# Decay rate D from Martínez et al. (1993)

D_MSH = np.random.lognormal(1.75, math.sqrt(2), 1) # MSH/day 
D = D_MSH*3e6 # km^2/day
print "Decay Rate (km^2/day):", D 

def spot_growth(max_area):
    # Describes sunspot growth during formation
    # ends on max_area that becomes initial_area in spot_decay

    t = 1 # days
    area = 3.9744*10**8*t # km^2, from Schlichenmaier et al. (2010)
    while area < max_area:
        area = 3.9744*10**8*t
        t += 1
        print "initial_area:", area

    else: 
        area = max_area
        print "initial_area:", area
    

def spot_decay(t, fracarea, star_surfarea):
    # time = 1, sun_surfarea = 6.1e12
    # Given initial fractional area (fracarea), compute spot dissolution

    initial_area = fracarea*(star_surfarea) # solar surface area (km^2)
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
    fracarea2 = spot_area/(star_surfarea) 
    print "Fractional Area (km^2)", fracarea2

    # in terms of theta
    r_star = math.sqrt(star_surfarea / 4*math.pi)
    r_spot = math.sqrt(spot_area / math.pi)

    theta = math.atan(r_spot / r_star)
    print "theta:", theta

    while fracarea2 > 0.000000001:
        return spot_decay(t, fracarea2, star_surfarea)

    else:
        fracraea2 = 0   
        
