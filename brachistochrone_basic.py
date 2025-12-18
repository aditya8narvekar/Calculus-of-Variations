# Numerical Solution to the problems in the Calculus of Variations

import numpy as np
from scipy import constants
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# first create an array containing values on the x-axis
N = 400      # number of points
x = np.linspace(0, 1, N)
dx = x[1]-x[0]

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
    y_full = np.concatenate(([1e-2], y, [1]))   # 1e-2 for ZeroDivisionError
    # now we construct our array of f(x,y,y')
    f = func(y_full)
    # finally we integrate this f over x
    return np.sum(f)*dx

result = minimize(time_taken, np.ones(N-2))

y = np.concatenate(([0],result.x,[1]))
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

# t here varies from t1 at (0,0) to t2 at (1,1)
# clearly, t1 = 0
# to find t2, divide x by y
# x/y = 1 = [t2 - sin(t2)] / [1 - cos(t2)]
# solving for t2 (numerically ofcourse), we get
t2 = 2.412011

# to find R, put values of y and t in first equation for point (1,1)
# 1 = R(1-cos(t2))
R = 1/(1-np.cos(t2))

# plot N points on the graph while varying t from t1 to t2

t = np.linspace(0, t2, N)
y_ideal = R * (1 - np.cos(t))
x_ideal = R * (t - np.sin(t))


#______________________________________________________________________________

# Now, we just need to plot the graphs.

plt.plot(x, -y, label='Numerical Solution', color='blue', linewidth=2.5)
plt.plot(x_ideal, -y_ideal, label='Exact Cycloid Solution', color='red', linewidth=2.5)

plt.title(f"Brachistochrone: Numerical vs Exact Solution (N={N})")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid()
plt.show()










    