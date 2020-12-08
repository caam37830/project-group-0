
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir
import numpy as np
import matplotlib.pyplot as plt

N = 10000
T = 100
I0 = 10
a_list = [0.8, 1.5, 8]
b_list = [0.1, 0.5, 1]
c_list = [0.1, 0.5, 0.8]
bal_state_list = []

# 1. a
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(15,5))
fig.suptitle("compare S,U,Q,C,I populations with different a",fontsize=20)

for i,a in enumerate(a_list):
    b = b_list[0]
    c = c_list[1]
    sol = SUQC_ODE_simulation(N,a,b,c,T,I0)
    bal_state_day = int(np.ceil(sol.t_events))
    bal_state_S = int(np.ceil(sol.y[0][bal_state_day]))
    bal_state_I = int(np.ceil(N - bal_state_S))
    bal_state_list.append([bal_state_day,bal_state_S,bal_state_I])

    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="unquarantined", c='r')
    ax[i].plot(sol.t, sol.y[2], label="quarantined", c='b')
    ax[i].plot(sol.t, sol.y[3], label="confirmed", c='y')
    ax[i].plot(sol.t, sol.y[1]+sol.y[2]+sol.y[3], label="infected", c='m')
    ax[i].set_title(f"a = {str(a_list[i])},b = {b},c={c}")

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('a =', a_list[i], 
          ', balance day =', bal_state_list[i][0],
          ', balance number of the susceptibles =', bal_state_list[i][1],
          ', balance number of the infected =', bal_state_list[i][2])
    
# 2. b
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(15,5))
fig.suptitle("compare S,U,Q,C,I populations with different b",fontsize=20)
bal_state_list = []

for i,b in enumerate(b_list):
    a = a_list[0]
    c = c_list[1]
    sol = SUQC_ODE_simulation(N,a,b,c,T,I0)
    bal_state_day = int(np.ceil(sol.t_events))
    bal_state_S = int(np.ceil(sol.y[0][bal_state_day]))
    bal_state_I = int(np.ceil(N - bal_state_S))
    bal_state_list.append([bal_state_day,bal_state_S,bal_state_I])
    
    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="unquarantined", c='r')
    ax[i].plot(sol.t, sol.y[2], label="quarantined", c='b')
    ax[i].plot(sol.t, sol.y[3], label="confirmed", c='y')
    ax[i].plot(sol.t, sol.y[1]+sol.y[2]+sol.y[3], label="infected", c='m')
    ax[i].set_title(f"a = {a},b = {str(b_list[i])},c={c}")
    
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('b =', b_list[i], 
          ', balance day =', bal_state_list[i][0],
          ', balance number of the susceptibles =', bal_state_list[i][1],
          ', balance number of the infected =', bal_state_list[i][2])
# 3. c
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(15,5))
fig.suptitle("compare S,U,Q,C,I populations with different c",fontsize=20)
bal_state_list = []

for i,c in enumerate(c_list):
    a = a_list[1]
    b = b_list[1]
    sol = SUQC_ODE_simulation(N,a,b,c,T,I0)
    bal_state_day = int(np.ceil(sol.t_events))
    bal_state_S = int(np.ceil(sol.y[0][bal_state_day]))
    bal_state_I = int(np.ceil(N - bal_state_S))
    bal_state_list.append([bal_state_day,bal_state_S,bal_state_I])
    
    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="unquarantined", c='r')
    ax[i].plot(sol.t, sol.y[2], label="quarantined", c='b')
    ax[i].plot(sol.t, sol.y[3], label="confirmed", c='y')
    ax[i].plot(sol.t, sol.y[1]+sol.y[2]+sol.y[3], label="infected", c='m')
    ax[i].set_title(f"a = {a},b = {b},c={str(c_list[i])}")
    
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('c =', c_list[i], 
          ', balance day =', bal_state_list[i][0],
          ', balance number of the susceptibles =', bal_state_list[i][1],
          ', balance number of the infected =', bal_state_list[i][2],)
