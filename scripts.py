from sir import *
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import MultipleLocator, FixedLocator, FixedFormatter

## Simulation

#### 1. Example plots of the S,I, and R populations over time for some choices of parameter b and k.

k_list = [0,1/6,1/3,1/2,2/3,5/6]
b_list = [1/6,1/3,1/2,2/3,5/6,1]
k_str = ['0','1/6','1/3','1/2','2/3','5/6']
b_str = ['1/6','1/3','1/2','2/3','5/6','1']
m, n = 6,6 # rows, columns of subplots
fig, ax = plt.subplots(6,6, figsize=(16,20))

N = 10000
T = 100
I0 = 10
for i in range(m):
    for j in range(n):
        b = b_list[i]
        k = k_list[j]
        sol = ODE_simulation(N,b,k,T,I0)
        ax[i,j].plot(sol.t, sol.y[0], label="susceptible", c='g')
        ax[i,j].plot(sol.t, sol.y[1], label="infectious", c='r')
        ax[i,j].plot(sol.t, sol.y[2], label="removed", c='b')
        ax[i,j].set_title(f"b = {str(b_str[i])},k = {k_str[j]}")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

#### 2. Phase diagrams for the discrete and ODE simulations

b_list = np.linspace(0,1,51)
k_list = np.linspace(0,1,51)
N = 10000
I0 = 10
I_sol_20 = np.zeros((len(b_list),len(k_list)))
I_sol_40 = np.zeros((len(b_list),len(k_list)))
I_sol_60 = np.zeros((len(b_list),len(k_list)))
T = 100
for i in range(len(b_list)):
    for j in range(len(k_list)):
        b = b_list[i]
        k = k_list[j]
        sol = ODE_simulation(N,b,k,T,I0)
        I_sol_20[i,j]=sol.y[1][19]
        I_sol_40[i,j]=sol.y[1][39]
        I_sol_60[i,j]=sol.y[1][59]


plt.figure(1,figsize=(14,4))
ax=plt.subplot(1,3,1)
plt.title("Phase diagram of infectious population on T = 20",fontsize=10,y=1.04)
plt.imshow(I_sol_20)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(14,4))
ax=plt.subplot(1,3,2)
plt.title("Phase diagram of infectious population on T = 40",fontsize=10,y=1.04)
plt.imshow(I_sol_40)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.figure(1,figsize=(14,4))
ax=plt.subplot(1,3,3)
plt.title("Phase diagram of infectious population on T = 60",fontsize=10,y=1.04)
plt.imshow(I_sol_60)
plt.colorbar()
ax.set_yticks(np.linspace(0,len(b_list)-1,len(b_list)//5+1))
ax.set_yticklabels(np.round(b_list[::5],2))
ax.set_xticks(np.linspace(0,len(k_list)-1,len(k_list)//5+1))
ax.set_xticklabels(np.round(k_list[::5],2))
plt.xlabel("k",fontsize=15,labelpad=5)
plt.ylabel("b",fontsize=15,labelpad=5)

plt.tight_layout()
plt.savefig('phase_diagram.png', dpi=300)
plt.show()
