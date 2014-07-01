import matplotlib.pyplot as plt
from pylab import *

import numpy as np
import numpy as np
 
data = np.loadtxt('tau_ceti_like/noisy/4660971.txt') 

t = data[:,1]
y = data[:,2]

def holt_winters_second_order_ewma(y, span, beta):
    N = y.size
    alpha = 2.0 / ( 1 + span )
    s = np.zeros(( N, ))
    b = np.zeros(( N, ))
    s[0] = y[0]
    for i in range( 1, N ):
        s[i] = alpha * y[i] + ( 1 - alpha )*( s[i-1] + b[i-1] )
        b[i] = beta * ( s[i] - s[i-1] ) + ( 1 - beta ) * b[i-1]
    return s

plt.plot(t, y, 'o', color = 'r')

# holt winters second order ewma
plt.plot( holt_winters_second_order_ewma( y, 10, 0.3 ), 'b', label='Holt-Winters' )
 
plt.title('Holt-Winters')
plt.legend( loc=8 )
plt.show()


