# Numerical Solution to the problems in the Calculus of Variations

# Version 2 (for a full curve)

import numpy as np
from scipy import constants
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# first create an array containing values on the x-axis
N = 600      # number of points
N_half = N//2
width = 5
x_half = np.linspace(0, width/2, N_half)
dx = x_half[1]-x_half[0]

def func(y):
    '''define your f(x,y,y') here'''
    # First we form the array of dy/dx
    dy_dx = np.diff(y) / dx
    
    # f(x,y,y') = (sqrt[1 + (y')^2] / sqrt[2gy])
    return (np.sqrt(1 + (dy_dx)**2) / np.sqrt(2*constants.g* np.abs(y[:-1])))
                                            # np.abs() to prevent -ve sqrt 

def time_taken(y):
    '''we are gonna define our integral here'''
    # First form the array of y
    y_full = np.concatenate(([1e-2], y, [2*width/(2*np.pi)]))   # 1e-2 for ZeroDivisionError
    # now we construct our array of f(x,y,y')
    f = func(y_full)
    # finally we integrate this f over x
    return np.sum(f)*dx

result = minimize(time_taken, np.ones(N_half-2))

y = np.concatenate(([0],result.x,[2*width/(2*np.pi)]))
print(result)


# Our work here is done, just plot x & y on a graph and you get the path of
# the cycloid. But for the sake of comparison, let's overlay the ideal path
# (i.e. the path of the cycloid) on our numerical solution graph.
# If you wish to use this code for problems other than the brachistochrone
# then just comment out the part below.


#______________________________________________________________________________
# Find x & y arrays ideal path (cycloid)

# for cycloid,
#   y = R(1-cos(t))
#   x = R(t-sin(t))

# 2*pi*R = width
R = width/(2*np.pi)

t = np.linspace(0, 2*np.pi, N)
y_ideal = R * (1 - np.cos(t))
x_ideal = R * (t - np.sin(t))


#______________________________________________________________________________

# Now, we just need to plot the graphs.

plt.plot(x_half, -y, label='Numerical Solution', color='blue', linewidth=2.5)

x_rest = x_half + width/2
y_rest = y[::-1]
plt.plot(x_rest, -y_rest, color='blue', linewidth=2.5)

plt.plot(x_ideal, -y_ideal, label='Exact Cycloid Solution', color='red', linewidth=2)

plt.axis('equal')
plt.title(f"Brachistochrone: Numerical vs Exact Solution (N={N})")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid()
plt.show()










    