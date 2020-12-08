import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import sir

N = 10000
b = 1/2
k = 1/20
T = 300
I0 = 10
p_list = np.linspace(0,1,10,endpoint = False)
m, n = 2,5
fig, ax = plt.subplots(m,n, figsize=(15,15))
fig.suptitle("S,I, and R populations over time for different p")
i = 0
j = 0
for p in p_list:
    counts_I,counts_R,counts_S = sir.sir_model_simulation_spatial(N, b, k, T, I0, p, 'center')
    ax[i,j].plot(counts_S,label="susceptible", c='r')
    ax[i,j].plot(counts_I,label="infectious", c='g')
    ax[i,j].plot(counts_R,label="removed", c='b')
    ax[i,j].set_title(f'p = {round(p,2)}')
    
    if j != 4:
        j+=1
    else:
        j=0
        i+=1
lines, labels = fig.axes[-2].get_legend_handles_labels()
fig.legend(lines, labels, loc = 'upper right')
plt.savefig('p1_discrete.png', dpi=300)
