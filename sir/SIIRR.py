import numpy as np
from numpy.random import randint, rand
import matplotlib.pyplot as plt
import random


class Person_variation3():
    """
    An agent representing a person.
    
    By default, a person is susceptible.  
    
    They can become removed using the remove method. 
    
    They can become infected using the infected mothod.
    
    """
    
    def __init__(self):
        self.state = "S" 
    
    def get_state(self):
        """
        returns the state of a person:"S","I1","I2","R1" or "R2"
        """
        return self.state
    
    def recover_1(self):
        """
        to make a person recovered
        """
        self.state = "R1"
        
    def dead(self):
        """
        to make a person die
        """
        self.state = "D"
        
    def remove_2(self):
        """
        to make a person recovered
        """
        self.state = "R2"
        
    def infected_1(self):
        """
        to make a person infectious of the original strain
        """
        self.state = "I1"
    
    def infected_2(self):
        """
        to make a person infectious of the new strain
        """
        self.state = "I2"
    
def count_infectious_1(pop):
    """
    count how many people are infectious of the original strain at the end of the day
    
    """
    return sum((p.get_state() == "I1") for p in pop)

def count_infectious_2(pop):
    """
    count how many people are infectious of the new strain at the end of the day
    
    """
    return sum((p.get_state() == "I2") for p in pop)

def count_recover(pop):
    """
    count how many people are recovered from the original strain at the end of the day
    
    """
    return sum((p.get_state() == "R1") for p in pop)

def count_dead(pop):
    """
    count how many people are dead caused by the original strain at the end of the day
    
    """
    return sum((p.get_state() == "D") for p in pop)

def count_susceptible(pop):
    """
    count how many people are susceptible at the end of the day
    
    """
    return sum((p.get_state() == "S") for p in pop)


def variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0):    
    """
    simulate a population, where people interact and change state according to the model parameters.
    
    N: N individuals the population has
    
    b: the number of interactions each day that could spread the disease (per individual) caused by the original strain
    
    k: the fraction of the infectious population which recovers each day (original strain)
    
    b_: the number of interactions each day that could spread the disease (per individual) caused by the new strain
    
    k_: the fraction of the infectious population which recovers each day (new strain)
    
    T1: simulation time period only original strain exists
    
    T2: simulation time period original strain and new strain both exist
    
    I0: Initial number of infectious individuals
    
    """
    
    pop = [Person_variation3() for i in range(N)] # our population
    initial = randint(N, size=I0)
    for j in initial:
        pop[j].infected_1()
    counts_I = [I0]
    counts_R = [0]
    counts_D = [0]
    counts_S = [N-I0]
    counts_I2 = [0]
    
    for t in range(T1):
        for i in range(N):
            if pop[i].get_state()=="I1":  
                
                contacts = randint(N, size=int(b)+1)
                if b >= 1:
                    for j in contacts[:-1]:
                        if pop[j].get_state()=="S":
                            pop[j].infected_1()
                            
                j = contacts[-1]
                if (rand() < (b-int(b))) and (pop[j].get_state()=="S"):
                    pop[j].infected_1()
                           
                
                if rand() < k:
                    pop[i].recover_1()
                    
            if pop[i].get_state()=="R1":
                if rand() < d:
                    pop[i].dead()
                
        # add to our counts
        counts_I.append(count_infectious_1(pop))
        counts_R.append(count_recover(pop))
        counts_S.append(count_susceptible(pop))
        counts_D.append(count_dead(pop))
        counts_I2.append(0)
        
############################################### new strain appears########################################
    sta  = np.array([pop[i].get_state() for i in range(N)])
    sus = np.where(sta!='I1')[0]

    
#     initial = randint(N, size=I0)
#     for j in initial:
#         pop[j].infected_2()
        
    initial = random.sample(list(sus), I0)
    for j in initial:
        pop[j].infected_2()
        
    
    
    for t in range(T2):
        for i in range(N):
            state = pop[i].get_state()
            
            if state=="I1":  
                contacts = randint(N, size=int(b)+1)
                if b >= 1:
                    for j in contacts[:-1]:
                        if pop[j].get_state()=="S":
                            pop[j].infected_1()
                            
                j = contacts[-1]
                if (rand() < (b-int(b))) and (pop[j].get_state()=="S"):
                    pop[j].infected_1()
                                           
                if rand() < k:
                    pop[i].recover_1()
                    
            if state=="I2":  
                
                contacts = randint(N, size=int(b_)+1)
                if b_ >= 1:
                    for j in contacts[:-1]:
                        if pop[j].get_state()=="S" or pop[j].get_state()=="R1":
                            pop[j].infected_2()
                            
                j = contacts[-1]
                if (rand() < (b_-int(b_))) and (pop[j].get_state()=="S" or pop[j].get_state()=="R1"):
                    pop[j].infected_2()
                           
                
                if rand() < k_:
                    pop[i].remove_2()
                    
            if state=="R1":
                if rand() < d:
                    pop[i].dead()
                
        # add to our counts
        counts_I.append(count_infectious_1(pop))
        counts_R.append(count_recover(pop))
        counts_S.append(count_susceptible(pop))
        counts_D.append(count_dead(pop))
        counts_I2.append(count_infectious_2(pop))
        
    return counts_I,counts_R,counts_S,counts_D,counts_I2
        


