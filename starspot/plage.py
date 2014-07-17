## WORK IN PROGRESS ##
# Written by Aida Behmard, 5/22/2014
# Program that adds plages to simulation

import numpy as np
import math
import random 

def plage(self, theta, phase, p_fracarea):
       # Given spherical coords, get absolute coords
       # Convention: theta is a latitude in degrees: 0 = equator, +90 = north pole
       # Phase is in periods: 0 = transit, 0.5 = opposition, 1 = next transit

