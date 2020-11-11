# unit tests

import unittest
from sir import *
import numpy as np

class TestPerson(unittest.TestCase):
    """
    Test of Person class methods
    """
    
    def setUp(self):
        ppl = Person()
        self.ppl = ppl
        
    def test_get_state(self):
        self.assertTrue(self.ppl.get_state() == 'S')
        
    def test_remove(self):
        self.ppl.remove()
        self.assertTrue(self.ppl.get_state() == 'R')
        
    def test_infected(self):
        self.ppl.infected()
        self.assertTrue(self.ppl.get_state() == 'I')
    

class TestSIR(unittest.TestCase):
    """
    Test of count functions
    """
    
    def setUp(self):
        self.pop = [Person() for i in range(30)]
        for i in range(10):
            self.pop[i].infected()
        for i in range(10, 20):
            self.pop[i].remove()
        
    def test_count_infectious(self):
        self.assertTrue(count_infectious(self.pop) == 10)

    def test_count_removed(self):
        self.assertTrue(count_removed(self.pop) == 10)
        
    def test_count_susceptible(self):
        self.assertTrue(count_susceptible(self.pop) == 10)
        
#     def test_sir_model_simulation(self):
#         N = 5000
#         b = 1/2
#         k = 1/3
#         T = 100
#         counts_I,counts_R,counts_S = sir_model_simulation(N, b, k, T) 
#         pass
        
    
class TestODE(unittest.TestCase):
    """
    Test of ODE simulation
    """
    
    def test_ODE_simulation1(self):
        N = 5000
        b = 1/2
        k = 1/3
        T = 100
        I0 = 5
        sol = ODE_simulation(N,b,k,T,I0)
        
        for j in range(1, 10):
            if j * 10 > len(sol.y[0])-1:
                continue
                
            s = sol.y[0][j * 10]
            s_hat = sol.y[0][j * 10 + 1]
            i = sol.y[1][j * 10]
            i_hat = sol.y[1][j * 10 + 1]
            r = sol.y[2][j * 10]
            r_hat = sol.y[2][j * 10 + 1]
            
            ds = -b * s * i
            di = b * s * i - k * i
            dr = k * i
            
            sdiff = np.abs((s_hat - s) - ds)
            idiff = np.abs((i_hat - i) - di)
            rdiff = np.abs((r_hat - r) - dr)
            
            print(sdiff, ds)
            print(idiff, di)
            print(rdiff, dr)
            
            self.assertTrue(sdiff < np.abs(ds) and idiff < np.abs(di) and rdiff < np.abs(dr))
            
            
    def test_ODE_simulation2(self):
        N = 10000
        b = 2/3
        k = 2/3
        T = 100
        I0 = 20
        sol = ODE_simulation(N,b,k,T,I0)
        
        for j in range(1, 10):
            if j * 10 > len(sol.y[0])-1:
                continue
                
            s = sol.y[0][j * 10]
            s_hat = sol.y[0][j * 10 + 1]
            i = sol.y[1][j * 10]
            i_hat = sol.y[1][j * 10 + 1]
            r = sol.y[2][j * 10]
            r_hat = sol.y[2][j * 10 + 1]
            
            ds = -b * s * i
            di = b * s * i - k * i
            dr = k * i
            
            sdiff = np.abs((s_hat - s) - ds)
            idiff = np.abs((i_hat - i) - di)
            rdiff = np.abs((r_hat - r) - dr)
            
            print(sdiff, ds)
            print(idiff, di)
            print(rdiff, dr)
            
            self.assertTrue(sdiff < np.abs(ds) and idiff < np.abs(di) and rdiff < np.abs(dr))
            
            
    