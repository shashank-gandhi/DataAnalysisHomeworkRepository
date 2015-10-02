#1.2c

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

q = np.array([[0.5, 2], [2, 5], [1, 3]])


def hill_func(p, x):
    '''
    Return Hill Function
    '''
    a, k = p

    return x**a / (k**a +x**a)


#     return a * (np.log(x) - np.log(k))

x = np.linspace(0, 100, 500)

y1 = hill_func(q[0], x)
y2 = hill_func(q[1], x)
y3 = hill_func(q[2], x)



plt.semilogx(x, y1, '-')
plt.semilogx(x, y2, '-')
plt.semilogx(x, y3, '-')

# plt.loglog(x, y1, '-')
# plt.loglog(x, y2, '-')
# plt.loglog(x, y3, '-')
plt.margins(x = 0.02, y = 0.02)
plt.xlabel(r'$x$')
plt.ylabel(r"$y$")
plt.legend(('y1', 'y2', 'y3'), loc='lower right',prop={"size":12})


plt.draw()
plt.show()
