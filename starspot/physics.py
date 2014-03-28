# physics.py: physical formulas

import numpy as np
from scipy.special import wofz

def eddington_limb_darkening(theta):
    # Computes limb darkening factor.
    # Eddington approximation method, Carroll & Ostlie (ch. 9, p. 266)
    # In: Incidence angle (ray to normal)
    # Out: Attenuation factor (0 to 1)
    return 0.4 + 0.6 * np.cos(theta)

def voigt(x,amp,pos,fwhm,shape):
    # Computes Voigt spectral profile.
    tmp = 1/special.wofz(np.zeros((len(x))) \
        +1j*np.sqrt(np.log(2.0))*shape).real
    tmp = tmp*amp* \
        wofz(2*np.sqrt(N.log(2.0))*(x-pos)/fwhm+1j* \
        np.sqrt(np.log(2.0))*shape).real
    return tmp
