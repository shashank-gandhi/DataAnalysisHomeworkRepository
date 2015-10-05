# 1.2b

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# JB's favorite Seaborn settings for notebooks
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18,
    'axes.facecolor': 'DFDFE5'}
sns.set_context('paper', rc=rc)


plt.close('all')

q = np.array([[2, 4], [0, 2], [1, 3]])

def cauchy_distr(p, x):
    '''
    return cauchy distribution
    '''
    a, b = p

    return b / (np.pi * (b**2 + (x - a)**2))

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
plt.legend((r'$\alpha = 2, \, \beta = 4$', r'$\alpha = 0, \, \beta = 2$', 
r'$\alpha = 1, \, \beta = 3$'), loc='upper right',prop={"size":12})
plt.draw()
plt.show()
