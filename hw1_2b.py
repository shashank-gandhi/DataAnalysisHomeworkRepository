# 1.2b

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import beeswarm as bs
import seaborn as sns
sns.set()

# JB's favorite Seaborn settings for notebooks
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18,
    'axes.facecolor': 'DFDFE5'}
sns.set_context('paper', rc=rc)


plt.close('all')

q = np.array([[2, 4, 5], [0, 2, 3], [1, 3, 4]])

def cauchy_distr(p, x):
    '''
    return cauchy distribution
    '''
    a, b, π = p

    return b / (π * (b**2 + (x - a)**2))

x = np.linspace(-7, 13, 100)

y1 = cauchy_distr(q[0], x)
y2 = cauchy_distr(q[1], x)
y3 = cauchy_distr(q[2], x)

plt.plot(x, y1, '-')
plt.plot(x, y2, '-')
plt.plot(x, y3, '-')
plt.margins(x = 0.02, y = 0.02)
plt.xlabel(r'$x$')
plt.ylabel(r"$y$")
plt.legend(('y1', 'y2', 'y3'), loc='upper right',prop={"size":12})
plt.draw()
plt.show()
