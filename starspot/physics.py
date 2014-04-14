# physics.py: physical formulas

import numpy as np
import math
from scipy.special import wofz

def eddington_limb_darkening(theta):
    # Computes limb darkening factor.
    # Eddington approximation method, Carroll & Ostlie (ch. 9, p. 266)
    # In: Incidence angle (ray to normal)
    # Out: Attenuation factor (0 to 1)

    # normalized so that integral is 1 on unit circle
    return ( 0.4 + 0.6*np.cos(theta) ) / ( 1.2*math.pi )

def voigt(x,amp,pos,fwhm,shape):
    # Computes Voigt spectral profile.
    tmp = 1/wofz(np.zeros((len(x))) \
        +1j*np.sqrt(np.log(2.0))*shape).real
    tmp = tmp*amp* \
        wofz(2*np.sqrt(np.log(2.0))*(x-pos)/fwhm+1j* \
        np.sqrt(np.log(2.0))*shape).real
    return tmp

default_limb_darkening = eddington_limb_darkening