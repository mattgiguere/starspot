# Written by Aida Behmard, 5/29/2014
# Program that adds time-varying component to starspot area
# Ref: "Living Reviews in Solar Physics"

import numpy as np
import math
import random 

# Donati  & Collier Cameron (1997):
# AB Doradus = K dwarf
# eq_rate = 12.2434 rad/d; diff_rate = 0.0564 rad/d

def rotation(eq_rate, pol_rate, theta): # theta = lat 
	diff_rate = eq_rate - pol_rate
	rot_rate = eq_rate - diff_rate*math.sin(theta)**2
	print "Rotation Rate", rot_rate
