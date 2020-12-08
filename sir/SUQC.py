## SUQC model

import numpy as np
from scipy.integrate import solve_ivp

def SUQC_ODE_simulation(N,a,b,c,T,I0):
    """
    An ODE simulation that model time dependent variables: S, I, R
    
    N: N individuals the population has
    
    a: the number of individuals infected by an unquarantined individual per day
    
    b: the rate at which the cases are confirmed
    
    c: the rate at which unquarantined and infected individuals get quarantined
    
    T: simulation time period
    
    I0: Initial number of infectious and unquarantined individuals
    
    """
    def f(t, v):
        """
        v = [S, U, Q, C]
        
        """
        dSdt = - (a * v[1] * v[0]) / N
        dUdt = (a * v[1] * v[0]) / N - c * v[1]
        dQdt = c * v[1] - b * v[2]
        dCdt = b * v[2]
        return [dSdt, dUdt, dQdt, dCdt]
    
    def bal_state(t, v):
        return (a * v[1] * v[0]) / N - 1
    
    v0 = [(N-I0),I0,0,0]
    t_span = [0,T]
    t_eval = list(range(T))
    sol = solve_ivp(f, t_span, v0, t_eval=t_eval, events=bal_state)
    return sol
