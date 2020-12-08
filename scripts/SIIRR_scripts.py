import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir

N = 10000
b = 3/5
k = 2/5
b_ = 3/5
k_ = 1/5
d = 0.02
T1 = 25
T2 = 100
I0 = 10
counts_I,counts_R,counts_S,counts_D,counts_I2 = sir.variation3_simulation(N, b, k, b_, k_, d, T1, T2, I0)
plt.plot(counts_S,label="susceptible", c='r')
plt.plot(counts_I,label="infectious_1", c='g')
plt.plot(counts_R,label="recover from origin", c='b')
plt.plot(counts_I2,label="infectious_2", c='y')
plt.legend()
