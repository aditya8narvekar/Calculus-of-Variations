# Numerical Solution to the problems in the Calculus of Variations
#   Shortest Distance

import numpy as np
from scipy import constants
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# create array containing values on the x-axis
N = 200      # number of points
x = np.linspace(0, 1, N)
dx = x[1]-x[0]

def func(y):
    ''' define f(x,y,y') '''
    # First we form the array of dy/dx
    dy_dx = np.diff(y) / dx     # array of slope at each point

    ## f(x,y,y') for minimal surface of rotation
    return np.sqrt(1 + dy_dx**2)

def functional(y):
    ''' define the integral: J[y] '''
    # First form the array of y
    y_full = np.concatenate(([0], y, [1]))
    
    # now we construct our array of f(x,y,y')
    f = func(y_full)
    
    # finally we integrate this f over x
    return np.sum(f)*dx

result = minimize(functional, np.ones(N-2))

y = np.concatenate(([0],result.x,[1]))
print(result)


# Now, we just need to plot the graphs.

plt.plot(x, y, color='blue', linewidth=2.5)
plt.axis('equal')
plt.title("Shortest distance between (0,0) & (1,1)")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid()
plt.show()






