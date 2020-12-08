## SIRDC continues ode model
import numpy as np
from scipy.integrate import solve_ivp

def SIRDC_ODE_simulation(N,beta,gamma,theta,delta,T,I0):
    """
    An ODE simulation that model time dependent variables: S, I, R, D, C
    
    N: N individuals the population has
    
    beta: a fixed number of interactions that spread the disease per day per infected individual
    
    gamma: a Poisson rate of infectiousness resolves
    
    theta: a fixed fraction of people exiting the resolving state
    
    delta: a fixed fraction of the resolved consequences being died per day
    
    T: simulation time period
    
    I0: Initial number of infectious and unquarantined individuals
    
    """
    def f(t, v):
        
        """
        v = [S, I, R, D, C]
        
        """
        dSdt = - (beta * v[0] * v[1]) / N
        dIdt = (beta * v[0] * v[1]) / N - gamma * v[1]
        dRdt = gamma * v[1] - theta * v[2]
        dDdt = delta * theta * v[2]
        dCdt = (1 - delta) * theta * v[2]
        return [dSdt, dIdt, dRdt, dDdt, dCdt]
    
    def equil_state(t, v):
        return (beta * v[0] * v[1]) / N - 1
    
    v0 = [(N-I0), I0, 0, 0, 0]
    t_span = [0,T]
    t_eval = list(range(T))
    sol = solve_ivp(f, t_span, v0, t_eval=t_eval, events=equil_state)
    return sol


def SIRDC_time_varying_simulation(N,gamma,theta,delta,T,I0):
    """
    An ODE simulation that model time dependent variables: S, I, R, D, C, beta
    
    N: N individuals the population has
    
    beta: a time varying number of interactions that spread the disease per infected individual
    
    gamma: a Poisson rate of infectiousness resolves
    
    theta: a fixed fraction of people exiting the resolving state
    
    delta: a fixed fraction of the resolved consequences being died per day
    
    T: simulation time period
    
    I0: Initial number of infectious and unquarantined individuals
    
    """
    def f(t, v):
        
        """
        v = [S, I, R, D, C, beta]
        
        """
        dbetadt = - np.exp(- N/v[1] - N*gamma/v[0]) 
        dSdt = - (v[5] * v[0] * v[1]) / N
        dIdt = (v[5] * v[0] * v[1]) / N - gamma * v[1]
        dRdt = gamma * v[1] - theta * v[2]
        dDdt = delta * theta * v[2]
        dCdt = (1 - delta) * theta * v[2]
        return [dSdt, dIdt, dRdt, dDdt, dCdt, dbetadt]
    
    def equil_state(t, v):
        return (v[5] * v[0] * v[1]) / N -1
    
    v0 = [(N-I0), I0, 0, 0, 0, 0.8]
    t_span = [0,T]
    t_eval = list(range(T))
    sol = solve_ivp(f, t_span, v0, t_eval=t_eval, events=equil_state)
    return sol