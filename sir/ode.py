import numpy as np
from scipy.integrate import solve_ivp

def ODE_simulation(N,b,k,T,I0):
    """
    An ODE simulation that model time dependent variables: S, I, R
    
    N: N individuals the population has
    
    b: the number of interactions each day that could spread the disease (per individual)
    
    k: the fraction of the infectious population which recovers each day
    
    T: simulation time period
    
    I0: Initial number of infectious individuals
    
    """
    def f(t, v):
        return [-b * v[0] * v[1], b * v[0] * v[1] - k * v[1], k * v[1]]
    
    v0 = [(N-I0)/N,I0/N,0] ## One person is infectious while others are susceptible
    t_span = [0,T]
    t_eval = list(range(T))
    sol = solve_ivp(f, t_span, v0, t_eval=t_eval)
    return sol