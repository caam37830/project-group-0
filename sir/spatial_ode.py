import numpy as np
from scipy.integrate import solve_ivp
from scipy.ndimage import laplace


def spatial_PDE(N,b,k,p,T,I0,M=200):
    """
    A spatial PDE simulation that model time dependent variables: S, I, R
    
    N: N individuals the population has
    
    b: the number of interactions each day that could spread the disease (per individual)
    
    k: the fraction of the infectious population which recovers each day
    
    T: simulation time period
    
    I0: Initial positions of infectious individuals
    
    M: size of grid
    
    """
    def laplace_flat(A):
        A = A.reshape((M,M))
        return laplace(A).flatten()
        
    def f(t,v):
        """
        v = [S, I, R]
        
        """
        # print(v.shape)
        S = v[:M**2]
        I = v[M**2:-M**2]
        R = v[-M**2:]
        
        # derivatives
        dSdt = -b * S * I + p * laplace_flat(S)
        dIdt = b * S * I - k * I + p * laplace_flat(I)
        dRdt = k * I + p * laplace_flat(R)
        
        return np.concatenate([dSdt, dIdt, dRdt],axis=None)
    
    
    # get intial S0 and R0 from I0
    S0 = np.ones((M*M))-I0
    R0 = np.zeros((M*M))
    
    # solve_ivp only accept 1d initial value, so conbine 3 1d array to 1
    v0 = np.concatenate([S0,I0,R0],axis=None)
    
    t_span = [0,T]
    t_eval = list(range(T))
    sol = solve_ivp(f, t_span, v0, t_eval=t_eval)
    return sol
