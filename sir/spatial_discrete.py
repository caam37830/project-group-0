import numpy as np
from numpy.random import randint, rand
from scipy.spatial import KDTree, cKDTree

class Person_spatial():
    """
    An agent representing a person.
    
    By default, a person is susceptible.  
    
    They can become removed using the remove method. 
    
    They can become infected using the infected mothod.
    
    """
    
    def __init__(self):
        self.state = "S" 
        self.pos = np.array([np.random.rand(),np.random.rand()])
    
    def get_state(self):
        """
        returns the state of a person:"S","I" or "R"
        """
        return self.state
    
    def remove(self):
        """
        to make a person recovered
        """
        self.state = "R"
        
    def infected(self):
        """
        to make a person infected
        """
        self.state = "I"
    
    def get_pos(self):
        """
        returns the position of a person
        """
        return self.pos
    
    def take_step(self,p):
        """
        each individual takes a step of length p in a random direction
        """
        dpos = np.random.randn(2)
        dpos = dpos / np.linalg.norm(dpos)
        temp = self.pos + dpos * p
        if temp[0]>= 0 and temp[0]<=1 and temp[1]>= 0 and temp[1]<=1:
            self.pos = temp
        
def count_infectious(pop):
    """
    count how many people are infectious at the end of the day
    
    """
    return sum((p.get_state() == "I") for p in pop)

def count_removed(pop):
    """
    count how many people are recovered at the end of the day
    
    """
    return sum((p.get_state() == "R") for p in pop)

def count_susceptible(pop):
    """
    count how many people are susceptible at the end of the day
    
    """
    return sum((p.get_state() == "S") for p in pop)


def sir_model_simulation_spatial(N, b, k, T, I0, p, init):    
    """
    simulate a population, where people interact and change state according to the model parameters.
    
    N: N individuals the population has
    
    b: the number of interactions each day that could spread the disease (per individual)
    
    k: the fraction of the infectious population which recovers each day
    
    T: simulation time period
    
    I0: Initial number of infectious individuals
    
    p: step length
    
    init: initial infected indivuduals start pos ('corner', 'center' or 'randomly')
    
    """
    ## Initialization
    q = np.sqrt(b/N/np.pi)
    pop = [Person_spatial() for i in range(N)] # our population
    X = np.array([pop[i].get_pos() for i in range(N)])
    tree = KDTree(X)
    if init=='center':
        x = np.array([[0.5,0.5]])
        ds, contacts =  tree.query(x, I0)
        if len(contacts)>0:
            contacts = contacts[0]
            
    elif init=='corner':
        x = np.array([[0,0]])
        ds, contacts =  tree.query(x, I0)
        if len(contacts)>0:
            contacts = contacts[0]
    
    elif init=='random':
        contacts = randint(N, size=I0)
        
    for j in contacts:
        pop[j].infected()
        
    counts_I = [count_infectious(pop)]
    counts_R = [count_removed(pop)]
    counts_S = [count_susceptible(pop)]
    
    ## After an individual takes the random step
    ## they interact with all other individuals within radius q
    for t in range(T):
        for i in range(N):
            pop[i].take_step(p)
            
        X = np.array([pop[i].get_pos() for i in range(N)])
        tree = KDTree(X)
        
        for i in range(N):
            if pop[i].get_state()=="I":
                contacts = tree.query_ball_point(pop[i].get_pos(), q) # finds neighbors in ball of radius q
                if len(contacts)>0:
                    if type(contacts[0]) is np.ndarray:
                        contacts = contacts[0]
                        for j in contacts:
                            if pop[j].get_state()=="S":
                                pop[j].infected() 
                                
                    else:
                        contacts = contacts[0]
                        if pop[contacts].get_state()=="S":
                            pop[contacts].infected() 
                            
                
                if rand() < k:
                    pop[i].remove()
                    
                
        # add to our counts
        counts_I.append(count_infectious(pop))
        counts_R.append(count_removed(pop))
        counts_S.append(count_susceptible(pop))
    return counts_I,counts_R,counts_S
