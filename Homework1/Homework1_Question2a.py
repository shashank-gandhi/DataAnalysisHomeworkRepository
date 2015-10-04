# Import needed modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# JB's favorite Seaborn settings for notebooks
rc = {'lines.linewidth': 2, 
      'axes.labelsize': 18, 
      'axes.titlesize': 18, 
      'axes.facecolor': 'DFDFE5'}
sns.set_context('notebook', rc=rc)
sns.set_style('darkgrid', rc=rc)

plt.close('all')

# Problem 1.2

# Set up an array of arrays containing three different example sets of 
# parameters for our function

# In each three-element array, the 0th element is a, the 1st element is 
# b, and the 2nd element is lambda

q = np.array([[0, 2, 2], [10, 2, 1.5], [20, 3, 1]])

def exponent_func(p, x):
    '''
    return exponent decay with background signal
    '''
    a, b, L = p

    return a + b * np.exp(-x / L)

# Make a set of evenly spaced points in x
x = np.linspace(-5.0, 5.0, 50)

# Compute y for each of our three example sets of parameters
y1 = exponent_func(q[0], x)
y2 = exponent_func(q[1], x)
y3 = exponent_func(q[2], x)

# Make smooth plots
plt.plot(x, y1, '-')
plt.plot(x, y2, '-')
plt.plot(x, y3, '-')
plt.margins(x = 0.02, y = 0.02)
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Add a legend (must update if the parameter values are changed)
plt.legend((r'$\alpha = 0, \, \beta = 2, \, \lambda = 2$', 
r'$\alpha = 10, \, \beta = 2, \, \lambda = 1.5$', 
r'$\alpha = 20, \, \beta = 3, \, \lambda = 1$'), loc='upper right',
prop={"size":12})

plt.draw()
plt.show()

