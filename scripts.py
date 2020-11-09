# all scripts used to run code

from sir import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# set parameters b and k here???
# b: the number of interactions each day that could spread the disease (per individual)
# k: the fraction of the infectious population which recovers each day

b = 
k = 

# v = (s, i, r)
def SIR(t, v):
    return np.array([-b * v[0] * v[1], k * v[1], b * v[0] * v[1] - k * v[1]])

v0 = 
t_span = 
t_eval = 

sol = solve_ivp(SIR, t_span, v0, t_eval)