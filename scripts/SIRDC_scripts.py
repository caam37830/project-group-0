import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir
import numpy as np
import matplotlib.pyplot as plt

beta_list = [0.8, 1.5, 8]
gamma_list = [0.15, 0.5, 0.6]
delta_list = [0.1, 0.2, 0.3]
theta_list = [0.01, 0.1, 0.5]

N = 10000
T = 100
I0 = 10

# different beta values
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,5))
fig.suptitle("compare S,I,R,D,C subpopulations with different beta", fontsize=20)

equil_state_list = []
for i,beta in enumerate(beta_list):
    gamma = gamma_list[0]
    delta = delta_list[0]
    theta = theta_list[1]
    sol = sir.SIRDC_ODE_simulation(N,beta,gamma,theta,delta,T,I0)
    equil_state_day = int(np.ceil(sol.t_events))
    equil_state_S = int(sol.y[0][equil_state_day])
    equil_state_I = int(sol.y[1][equil_state_day])
    equil_state_R = int(sol.y[2][equil_state_day])
    equil_state_D = int(sol.y[3][equil_state_day])
    equil_state_C = int(N - equil_state_S - equil_state_I - equil_state_R - equil_state_D)
    equil_state_list.append([equil_state_day,equil_state_S,equil_state_I,equil_state_R,equil_state_D,equil_state_C])

    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="infected", c='r')
    ax[i].plot(sol.t, sol.y[2], label="resolved", c='b')
    ax[i].plot(sol.t, sol.y[3], label="died", c='y')
    ax[i].plot(sol.t, sol.y[4], label="recovered", c='m')
    ax[i].set_title(f"beta = {beta_list[i]},gamma = {gamma},delta={delta},theta = {theta}")

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('For beta =', beta_list[i], 
          ', on Day', equil_state_list[i][0],
          ', number of susceptibles stays constant at', equil_state_list[i][1],
          ', with number of infected to be', equil_state_list[i][2],
          ', number of resolved to be', equil_state_list[i][3],
          ', number of died to be', equil_state_list[i][4],
          'and number of recovered to be', equil_state_list[i][5])
    
#different gamma values
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,5))
fig.suptitle("compare S,I,R,D,C subpopulations with different gamma", fontsize=20)

equil_state_list = []
for i,gamma in enumerate(gamma_list):
    beta = beta_list[0]
    delta = delta_list[0]
    theta = theta_list[1]
    sol = sir.SIRDC_ODE_simulation(N,beta,gamma,theta,delta,T,I0)
    equil_state_day = int(np.ceil(sol.t_events))
    equil_state_S = int(sol.y[0][equil_state_day])
    equil_state_I = int(sol.y[1][equil_state_day])
    equil_state_R = int(sol.y[2][equil_state_day])
    equil_state_D = int(sol.y[3][equil_state_day])
    equil_state_C = int(N - equil_state_S - equil_state_I - equil_state_R - equil_state_D)
    equil_state_list.append([equil_state_day,equil_state_S,equil_state_I,equil_state_R,equil_state_D,equil_state_C])

    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="infected", c='r')
    ax[i].plot(sol.t, sol.y[2], label="resolved", c='b')
    ax[i].plot(sol.t, sol.y[3], label="died", c='y')
    ax[i].plot(sol.t, sol.y[4], label="recovered", c='m')
    ax[i].set_title(f"beta = {beta},gamma = {gamma_list[i]},delta={delta},theta = {theta}")

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('For gamma =', gamma_list[i], 
          ', on Day', equil_state_list[i][0],
          ', number of susceptibles stays constant at', equil_state_list[i][1],
          ', with number of infected to be', equil_state_list[i][2],
          ', number of resolved to be', equil_state_list[i][3],
          ', number of died to be', equil_state_list[i][4],
          'and number of recovered to be', equil_state_list[i][5])
    
    
# different theta values
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,5))
fig.suptitle("compare S,I,R,D,C subpopulations with different theta", fontsize=20)

equil_state_list = []
for i,theta in enumerate(theta_list):
    beta = beta_list[0]
    delta = delta_list[0]
    gamma = gamma_list[0]
    sol = sir.SIRDC_ODE_simulation(N,beta,gamma,theta,delta,T,I0)
    equil_state_day = int(np.ceil(sol.t_events))
    equil_state_S = int(sol.y[0][equil_state_day])
    equil_state_I = int(sol.y[1][equil_state_day])
    equil_state_R = int(sol.y[2][equil_state_day])
    equil_state_D = int(sol.y[3][equil_state_day])
    equil_state_C = int(N - equil_state_S - equil_state_I - equil_state_R - equil_state_D)
    equil_state_list.append([equil_state_day,equil_state_S,equil_state_I,equil_state_R,equil_state_D,equil_state_C])

    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="infected", c='r')
    ax[i].plot(sol.t, sol.y[2], label="resolved", c='b')
    ax[i].plot(sol.t, sol.y[3], label="died", c='y')
    ax[i].plot(sol.t, sol.y[4], label="recovered", c='m')
    ax[i].set_title(f"beta = {beta},gamma = {gamma},delta={delta},theta = {theta_list[i]}")

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('For theta =', theta_list[i], 
          ', on Day', equil_state_list[i][0],
          ', number of susceptibles stays constant at', equil_state_list[i][1],
          ', with number of infected to be', equil_state_list[i][2],
          ', number of resolved to be', equil_state_list[i][3],
          ', number of died to be', equil_state_list[i][4],
          'and number of recovered to be', equil_state_list[i][5])
    
#different delta values
m, n = 1,3 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,5))
fig.suptitle("compare S,I,R,D,C subpopulations with different delta", fontsize=20)

equil_state_list = []
for i,delta in enumerate(delta_list):
    beta = beta_list[0]
    theta = theta_list[1]
    gamma = gamma_list[0]
    sol = sir.SIRDC_ODE_simulation(N,beta,gamma,theta,delta,T,I0)
    equil_state_day = int(np.ceil(sol.t_events))
    equil_state_S = int(sol.y[0][equil_state_day])
    equil_state_I = int(sol.y[1][equil_state_day])
    equil_state_R = int(sol.y[2][equil_state_day])
    equil_state_D = int(sol.y[3][equil_state_day])
    equil_state_C = int(N - equil_state_S - equil_state_I - equil_state_R - equil_state_D)
    equil_state_list.append([equil_state_day,equil_state_S,equil_state_I,equil_state_R,equil_state_D,equil_state_C])

    ax[i].plot(sol.t, sol.y[0], label="susceptible", c='g')
    ax[i].plot(sol.t, sol.y[1], label="infected", c='r')
    ax[i].plot(sol.t, sol.y[2], label="resolved", c='b')
    ax[i].plot(sol.t, sol.y[3], label="died", c='y')
    ax[i].plot(sol.t, sol.y[4], label="recovered", c='m')
    ax[i].set_title(f"beta = {beta},gamma = {gamma},delta={delta_list[i]},theta = {theta}")

lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines,labels,bbox_to_anchor=(1.01, 0.9), loc = 'upper right')

for i in range(3):
    print('For theta =', theta_list[i], 
          ', on Day', equil_state_list[i][0],
          ', number of susceptibles stays constant at', equil_state_list[i][1],
          ', with number of infected to be', equil_state_list[i][2],
          ', number of resolved to be', equil_state_list[i][3],
          ', number of died to be', equil_state_list[i][4],
          'and number of recovered to be', equil_state_list[i][5])
    
#time-varying beta
gamma = gamma_list[0]
delta = delta_list[0]
theta = theta_list[1]

sol = sir.SIRDC_time_varying_simulation(N,gamma,theta,delta,T,I0)

plt.plot(sol.t, sol.y[5])
plt.title('time-varying beta with quarantine being practiced')
plt.show()
plt.plot(sol.t, sol.y[0], label="susceptible", c='g')
plt.plot(sol.t, sol.y[1], label="infected", c='r')
plt.plot(sol.t, sol.y[2], label="resolved", c='b')
plt.plot(sol.t, sol.y[3], label="died", c='y')
plt.plot(sol.t, sol.y[4], label="recovered", c='m')
plt.legend(bbox_to_anchor=(1.01, 0.8), loc = 'upper right')

equil_state_list = []
equil_state_day = int(np.ceil(sol.t_events))
equil_state_S = int(sol.y[0][equil_state_day])
equil_state_I = int(sol.y[1][equil_state_day])
equil_state_R = int(sol.y[2][equil_state_day])
equil_state_D = int(sol.y[3][equil_state_day])
equil_state_C = int(N - equil_state_S - equil_state_I - equil_state_R - equil_state_D)
equil_state_list = [equil_state_day,equil_state_S,equil_state_I,equil_state_R,equil_state_D,equil_state_C]
print('On Day', equil_state_list[0],
      ', number of susceptibles stays constant at', equil_state_list[1],
      ', with number of infected to be', equil_state_list[2],
      ', number of resolved to be', equil_state_list[3],
      ', number of died to be', equil_state_list[4],
      'and number of recovered to be', equil_state_list[5])