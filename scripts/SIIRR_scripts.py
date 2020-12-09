import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir
import matplotlib.pyplot as plt

T1_list = [5,10,15,20,25,30,35,40]
N = 10000
b = 3/5
k = 2/5
b_ = 1
k_ = 1/5
d = 0.02
T2 = 100
I0 = 10

m, n = 2,4
fig, ax = plt.subplots(m,n, figsize=(15,7))
fig.suptitle("S,I, and R populations over time for different time the new strain appears")
i = 0
j = 0
for T1 in T1_list:
    counts_I1,counts_R1,counts_S,counts_D1,counts_I2 = sir.variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0)
    ax[i,j].plot(counts_S,label="susceptible", c='r')
    ax[i,j].plot(counts_I1,label="infectious1", c='g')
    ax[i,j].plot(counts_I2,label="infectious2", c='y')
    ax[i,j].plot(counts_R1,label="removed1", c='b')
    ax[i,j].set_title(f'T1 = {T1}')
    if j != 3:
        j+=1
    else:
        j=0
        i+=1
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'upper right')
plt.savefig('variation3.png', dpi=300)

N = 10000
b = 3/5
k = 2/5

d = 0.02
T1 = 30
T2 = 300
I0 = 10
m, n = 1,3
fig, ax = plt.subplots(m,n, figsize=(15,5))
fig.suptitle("S,I, and R populations over time for different b' and k'")

b_ = 3/5
k_ = 2/5
counts_I1,counts_R1,counts_S,counts_D1,counts_I2 = sir.variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0)
ax[0].plot(counts_S,label="susceptible", c='r')
ax[0].plot(counts_I1,label="infectious1", c='g')
ax[0].plot(counts_I2,label="infectious2", c='y')
ax[0].plot(counts_R1,label="removed1", c='b')
ax[0].set_title(f"b' = {b_},k' = {k_}")

b_ = 4/5
k_ = 2/5
counts_I1,counts_R1,counts_S,counts_D1,counts_I2 = sir.variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0)
ax[1].plot(counts_S,label="susceptible", c='r')
ax[1].plot(counts_I1,label="infectious1", c='g')
ax[1].plot(counts_I2,label="infectious2", c='y')
ax[1].plot(counts_R1,label="removed1", c='b')
ax[1].set_title(f"b' = {b_},k' = {k_}")

b_ = 3/5
k_ = 1/5
counts_I1,counts_R1,counts_S,counts_D1,counts_I2 = sir.variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0)
ax[2].plot(counts_S,label="susceptible", c='r')
ax[2].plot(counts_I1,label="infectious1", c='g')
ax[2].plot(counts_I2,label="infectious2", c='y')
ax[2].plot(counts_R1,label="removed1", c='b')
ax[2].set_title(f"b' = {b_},k' = {k_}")
                  
lines, labels = fig.axes[-1].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'upper right')
plt.savefig('variation3_2.png', dpi=300)
    
