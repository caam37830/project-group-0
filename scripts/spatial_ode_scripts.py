import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir
import numpy as np
from scipy.sparse import csgraph
from scipy.integrate import solve_ivp
import scipy.linalg as la
import matplotlib.pyplot as plt
from scipy.ndimage import laplace
from numpy.random import randint, rand
from tqdm import tqdm


### infected individuals start at the center of the square

k = 0.4
b = 0.6

M = 100
T = 150
N = M**2
# grids with 1s and 0s, 1s are the infected
# i0 = M # number of the infected
# I0 = np.random.choice([1]*i0+[0]*(M*M-i0), size=(M**2), replace=False)
I0 = np.zeros((M,M))
midpart = (np.random.rand(5,5)>0.5)*1
I0[48:53,48:53] = midpart[:,:]
I0 = I0.flatten()
       
p_list = [1,10,20,30,40,50]
fig, ax = plt.subplots(2,3, figsize=(21,14))

fig.suptitle("S,I, and R populations with diffenert step size p",fontsize=20)

I_max = []
I_max_t = []
total_infect = []

for ind in tqdm(range(len(p_list))):
      
    i = ind//3
    j = ind%3
    p = p_list[ind]
    sol = spatial_PDE(N,b,k,p,T,I0,M=M)

    S = []
    I = []
    R = []
    for dayind in range(T):
        S.append(np.sum(sol.y[:,dayind][:M**2]))
        I.append(np.sum(sol.y[:,dayind][M**2:-M**2]))
        R.append(np.sum(sol.y[:,dayind][-M**2:]))
    
    Imax = np.max(I)
    I_max.append(Imax)
    I_max_t.append(I.index(Imax))
    total_infect.append(I[-1]+R[-1])
    
    ax[i,j].plot(list(range(T)), S, label="susceptible", c='g')
    ax[i,j].plot(list(range(T)), I, label="infectious", c='r')
    ax[i,j].plot(list(range(T)), R, label="removed", c='b')

    ax[i,j].set_title(f"p = {p/100}",fontsize=10)
        
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(1.01, 0.9),loc = 'upper right')

for p in range(6):
    if p==0:
        print('p =', 0.01)
    else:
        print('p =', p*10)
    print('maxima of I:', I_max[p])
    print('time that maxima appears:', I_max_t[p])
    print('total number of infected individual(I+R):', total_infect[p])
    print()
    
### compare between different I0

### infected individuals start at the center of the square

k = 0.4
b = 0.6
M = 100
N = M**2
T = 300
p = 1

fig, ax = plt.subplots(1,3, figsize=(15,5))
fig.suptitle("S,I, and R populations with different position of I0",fontsize=20)

# grids with 1s and 0s, 1s are the infected

midpart = (np.random.rand(5,5)>0.5)*1
i0 = np.sum(midpart) # number of the infected

I_max = []
I_max_t = []
total_infect = []

## 0
I0 = np.zeros((M,M))
I0[0:5,0:5] = midpart[:,:]
I0 = I0.flatten()       
        
sol = spatial_PDE(N,b,k,p,T,I0,M)

S = []
I = []
R = []
for dayind in range(T):
    S.append(np.sum(sol.y[:,dayind][:M**2]))
    I.append(np.sum(sol.y[:,dayind][M**2:-M**2]))
    R.append(np.sum(sol.y[:,dayind][-M**2:]))

Imax = np.max(I)
I_max.append(Imax)
I_max_t.append(I.index(Imax))
total_infect.append(I[-1]+R[-1])

ax[0].plot(list(range(T)), S, label="susceptible", c='g')
ax[0].plot(list(range(T)), I, label="infectious", c='r')
ax[0].plot(list(range(T)), R, label="removed", c='b')
ax[0].set_title(f"I0 at corner",fontsize=10)

## 1
I0 = np.zeros((M,M))
I0[48:53,48:53] = midpart[:,:]
I0 = I0.flatten()       
        
sol = spatial_PDE(N,b,k,p,T,I0,M)

S = []
I = []
R = []
for dayind in range(T):
    S.append(np.sum(sol.y[:,dayind][:M**2]))
    I.append(np.sum(sol.y[:,dayind][M**2:-M**2]))
    R.append(np.sum(sol.y[:,dayind][-M**2:]))

Imax = np.max(I)
I_max.append(Imax)
I_max_t.append(I.index(Imax))  
total_infect.append(I[-1]+R[-1])
    
ax[1].plot(list(range(T)), S, label="susceptible", c='g')
ax[1].plot(list(range(T)), I, label="infectious", c='r')
ax[1].plot(list(range(T)), R, label="removed", c='b')
ax[1].set_title(f"I0 at center",fontsize=10)

## 2
I0 = np.random.choice([1]*i0+[0]*(M*M-i0), size=(M**2), replace=False)      
        
sol = spatial_PDE(N,b,k,p,T,I0,M)

S = []
I = []
R = []
for dayind in range(T):
    S.append(np.sum(sol.y[:,dayind][:M**2]))
    I.append(np.sum(sol.y[:,dayind][M**2:-M**2]))
    R.append(np.sum(sol.y[:,dayind][-M**2:]))

Imax = np.max(I)
I_max.append(Imax)
I_max_t.append(I.index(Imax))
total_infect.append(I[-1]+R[-1])
    
ax[2].plot(list(range(T)), S, label="susceptible", c='g')
ax[2].plot(list(range(T)), I, label="infectious", c='r')
ax[2].plot(list(range(T)), R, label="removed", c='b')
ax[2].set_title(f"I0 randomly spread out",fontsize=10)

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, bbox_to_anchor=(1.01, 0.9),loc = 'upper right')

title = ['I0 at corner', 'I0 at center', 'I0 redomly spread out']
for i in range(3):
    print(title[i])
    print('maxima of I:', I_max[i])
    print('time that maxima appears:', I_max_t[i])
    print('total number of infected individual(I+R):', total_infect[i])
    print()