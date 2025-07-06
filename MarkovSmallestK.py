# %%
### Markov Chains - smallest k for which the distribution is approximately steady state
import numpy as np

# Transition matrix for the Markov chain
T_matrix = np.array([[0.6, 0.4, 0,0],
                     [0.7, 0.3, 0,0],
                     [0,0,0.4, 0.6],
                     [0,0,0.2, 0.8]])

# Initial distribution
distro = np.array([0.2, 0.6, 0.19, 0.01])

# Calculate an approximate steady state distribution
steady_state = np.linalg.matrix_power(T_matrix,1000) @ distro

# Number of decimal places to round to
n = 8

# Rounds a number to n decimal places
def rounder(x, n):
    for i in range(len(x)):
        x[i] = round(x[i], n)
    return x

steady_state = rounder(steady_state, n)

k=0
iter = np.array([0])
for k in range(1000):
    approx = True
    iter = np.linalg.matrix_power(T_matrix,k) @ distro # calculates the distribution after k iterations
    for i in range(len(iter)):
        iter[i] = round(iter[i], n)
        if iter[i]==steady_state[i]:
            approx = True
        else:
            approx = False
            break
    if approx:
        print("k =", k)
        break
print("Steady state distribution:", steady_state)
print("Approximate steady state distribution:", iter)


