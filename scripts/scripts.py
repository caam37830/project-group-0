import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import MultipleLocator, FixedLocator, FixedFormatter

## Discrete Simulation
#### 1. Example plots of the S,I, and R populations over time for some choices of parameter b and k.

k_list = [1/5,2/5,3/5,4/5]
b_list = [1/5,2/5,3/5,4/5,1,2]
k_str = ['1/5','2/5','3/5','4/5']
b_str = ['1/5','2/5','3/5','4/5','1','2']
m, n = 4,6 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,15))

N = 10000
T = 100
I0 = 10
fig.suptitle("S,I, and R populations over time")
for i in range(m):
    for j in range(n):
        k = k_list[i]
        b = b_list[j]
        counts_I,counts_R,counts_S = sir.sir_model_simulation(N, b, k, T,I0) 
        ax[i,j].plot(np.array(counts_S)/N, label="susceptible", c='g')
        ax[i,j].plot(np.array(counts_I)/N, label="infectious", c='r')
        ax[i,j].plot(np.array(counts_R)/N, label="removed", c='b')
        ax[i,j].set_title(f"b = {str(b_str[j])},k = {k_str[i]}")
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'upper right')
plt.savefig('Example_plot_discrete.png', dpi=300)

#### 2. Phase diagrams for the discrete and ODE simulations
b_list = np.linspace(0,1,51)
k_list = np.linspace(0,1,51)
N = 10000
I0 = 10
counts_S_20 = np.zeros((len(b_list),len(k_list)))
counts_S_40 = np.zeros((len(b_list),len(k_list)))
counts_S_60 = np.zeros((len(b_list),len(k_list)))
counts_S_80 = np.zeros((len(b_list),len(k_list)))
counts_I_20 = np.zeros((len(b_list),len(k_list)))
counts_I_40 = np.zeros((len(b_list),len(k_list)))
counts_I_60 = np.zeros((len(b_list),len(k_list)))
counts_I_80 = np.zeros((len(b_list),len(k_list)))
counts_R_20 = np.zeros((len(b_list),len(k_list)))
counts_R_40 = np.zeros((len(b_list),len(k_list)))
counts_R_60 = np.zeros((len(b_list),len(k_list)))
counts_R_80 = np.zeros((len(b_list),len(k_list)))
T = 80
for i in range(len(b_list)):
    for j in range(len(k_list)):
        b = b_list[i]
        k = k_list[j]
        counts_I,counts_R,counts_S = sir.sir_model_simulation(N, b, k, T,I0)
        counts_S_20[i,j]=counts_S[19]/N
        counts_S_40[i,j]=counts_S[39]/N
        counts_S_60[i,j]=counts_S[59]/N
        counts_S_80[i,j]=counts_S[79]/N
        counts_I_20[i,j]=counts_I[19]/N
        counts_I_40[i,j]=counts_I[39]/N
        counts_I_60[i,j]=counts_I[59]/N
        counts_I_80[i,j]=counts_I[79]/N
        counts_R_20[i,j]=counts_R[19]/N
        counts_R_40[i,j]=counts_R[39]/N
        counts_R_60[i,j]=counts_R[59]/N
        counts_R_80[i,j]=counts_R[79]/N
    
plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Susceptible population on T = 20",fontsize=20,y=1.04)
plt.imshow(counts_S_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Susceptible population on T = 40",fontsize=20,y=1.04)
plt.imshow(counts_S_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Susceptible population on T = 60",fontsize=20,y=1.04)
plt.imshow(counts_S_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Susceptible population on T = 80",fontsize=20,y=1.04)
plt.imshow(counts_S_80)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram_discrete_S.png', dpi=300)
plt.show()

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Infectious population on T = 20",fontsize=20,y=1.04)
plt.imshow(counts_I_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Infectious population on T = 40",fontsize=20,y=1.04)
plt.imshow(counts_I_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Infectious population on T = 60",fontsize=20,y=1.04)
plt.imshow(counts_I_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Infectious population on T = 80",fontsize=20,y=1.04)
plt.imshow(counts_I_80)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram_discrete_I.png', dpi=300)
plt.show()

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Removed population on T = 20",fontsize=20,y=1.04)
plt.imshow(counts_R_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Removed population on T = 40",fontsize=20,y=1.04)
plt.imshow(counts_R_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Removed population on T = 60",fontsize=20,y=1.04)
plt.imshow(counts_R_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Removed population on T = 80",fontsize=20,y=1.04)
plt.imshow(counts_R_80)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram_discrete_R.png', dpi=300)
plt.show()


## ODE Simulation
#### 1. Example plots of the S,I, and R populations over time for some choices of parameter b and k.
k_list = [1/5,2/5,3/5,4/5]
b_list = [1/5,2/5,3/5,4/5,1,3]
k_str = ['1/5','2/5','3/5','4/5']
b_str = ['1/5','2/5','3/5','4/5','1','3']
m, n = 4,6 # rows, columns of subplots
fig, ax = plt.subplots(m,n, figsize=(20,15))

N = 10000
T = 100
I0 = 10
fig.suptitle("S,I, and R populations over time (ODE)",fontsize=15)
for i in range(m):
    for j in range(n):
        k = k_list[i]
        b = b_list[j]
        sol = sir.ODE_simulation(N,b,k,T,I0)
        ax[i,j].plot(sol.t, sol.y[0], label="susceptible", c='g')
        ax[i,j].plot(sol.t, sol.y[1], label="infectious", c='r')
        ax[i,j].plot(sol.t, sol.y[2], label="removed", c='b')
        ax[i,j].set_title(f"b = {str(b_str[j])},k = {k_str[i]}",fontsize=10)
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'upper right')
plt.savefig('Example_plot_ode.png', dpi=300)

#### 2. Phase diagrams for the discrete and ODE simulations

b_list = np.linspace(0,1,51)
k_list = np.linspace(0,1,51)
N = 10000
I0 = 10
I_sol_20 = np.zeros((len(b_list),len(k_list)))
I_sol_40 = np.zeros((len(b_list),len(k_list)))
I_sol_60 = np.zeros((len(b_list),len(k_list)))
I_sol_80 = np.zeros((len(b_list),len(k_list)))
S_sol_20 = np.zeros((len(b_list),len(k_list)))
S_sol_40 = np.zeros((len(b_list),len(k_list)))
S_sol_60 = np.zeros((len(b_list),len(k_list)))
S_sol_80 = np.zeros((len(b_list),len(k_list)))
R_sol_20 = np.zeros((len(b_list),len(k_list)))
R_sol_40 = np.zeros((len(b_list),len(k_list)))
R_sol_60 = np.zeros((len(b_list),len(k_list)))
R_sol_80 = np.zeros((len(b_list),len(k_list)))
T = 80
for i in range(len(b_list)):
    for j in range(len(k_list)):
        b = b_list[i]
        k = k_list[j]
        sol = ODE_simulation(N,b,k,T,I0)
        S_sol_20[i,j]=sol.y[0][19]
        S_sol_40[i,j]=sol.y[0][39]
        S_sol_60[i,j]=sol.y[0][59]
        S_sol_80[i,j]=sol.y[0][79]
        I_sol_20[i,j]=sol.y[1][19]
        I_sol_40[i,j]=sol.y[1][39]
        I_sol_60[i,j]=sol.y[1][59]
        I_sol_80[i,j]=sol.y[1][79]
        R_sol_20[i,j]=sol.y[2][19]
        R_sol_40[i,j]=sol.y[2][39]
        R_sol_60[i,j]=sol.y[2][59]
        R_sol_80[i,j]=sol.y[2][79]

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Susceptible population on T = 20",fontsize=20,y=1.04)
plt.imshow(S_sol_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Susceptible population on T = 40",fontsize=20,y=1.04)
plt.imshow(S_sol_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Susceptible population on T = 60",fontsize=20,y=1.04)
plt.imshow(S_sol_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Susceptible population on T = 80",fontsize=20,y=1.04)
plt.imshow(S_sol_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram_ode_S.png', dpi=300)
plt.show()


plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Infectious population on T = 20",fontsize=20,y=1.04)
plt.imshow(I_sol_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Infectious population on T = 40",fontsize=20,y=1.04)
plt.imshow(I_sol_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Infectious population on T = 60",fontsize=20,y=1.04)
plt.imshow(I_sol_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Infectious population on T = 80",fontsize=20,y=1.04)
plt.imshow(I_sol_80)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram_ode_I.png', dpi=300)
plt.show()

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,1)
plt.title("Removed population on T = 20",fontsize=20,y=1.04)
plt.imshow(R_sol_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,2)
plt.title("Removed population on T = 40",fontsize=20,y=1.04)
plt.imshow(R_sol_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,3)
plt.title("Removed population on T = 60",fontsize=20,y=1.04)
plt.imshow(R_sol_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(24,6))
ax=plt.subplot(1,4,4)
plt.title("Removed population on T = 80",fontsize=20,y=1.04)
plt.imshow(R_sol_80)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)
 
plt.tight_layout()
plt.savefig('phase_diagram_ode_R.png')
plt.show()

