import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import beeswarm as bs
import seaborn as sns
sns.set()

plt.close('all')


#1.2

# def exponent_func(p, x):
#     '''
#     return exponent decay with background
#     '''
#     a, b, l = p

#     return a + b * np.exp(-x / l)

# x = np.linspace(-5.0, 5.0, 50)

# y = exponent_func(np.array([2, 4, 2]), x)

# plt.plot(x, y, 'o')
# plt.margins(x = 0.02, y = 0.02)
# plt.xlabel(r'$x')
# plt.ylabel(r'$y')

# plt.draw()
# plt.show()

#1.2b

# def cauchy_distr(p, x):
#     '''
#     return cauchy distribution
#     '''
#     a, b, π = p

#     return b / (π * (b**2 + (x - a)**2))

# x = np.linspace(-7, 13, 100)

# y = cauchy_distr(np.array([3, 2, 5]), x)

# plt.plot(x, y, 'o')
# plt.margins(x = 0.02, y = 0.02)
# plt.xlabel(r'$x')
# plt.ylabel(r'$y')

# plt.draw()
# plt.show()

#1.2c

# def hill_func(p, x):
#     '''
#     Return Hill Function
#     '''
#     a, k = p

#     return x**a / (k**a +x**a)

# x = np.linspace(-5.0, 5.0, 50)

# y = hill_func(np.array([4, 8]), x)

# plt.plot(x, y, 'o')
# plt.margins(x = 0.02, y = 0.02)
# plt.xlabel(r'$x')
# plt.ylabel(r'$y')

# plt.draw()
# plt.show()

# 1.3

# read the csv into a dataframe
df = pd.read_csv('gardner_et_al_2011_time_to_catastrophe_dic.csv', comment = '#')

# This data is not tidy because each row is not an observation

# splice the data tables

df['time to catastrophe with labeled tubulin (s)']
df['time to catastrophe with unlabeled tubulin (s)']


# Drop all NaN values
df['time to catastrophe with unlabeled tubulin (s)'].dropna()

#plot the two data sets

# _ = plt.hist(df['time to catastrophe with labeled tubulin (s)'], bins = 20, normed = False, alpha = 0.75)
# _ = plt.hist(df['time to catastrophe with unlabeled tubulin (s)'].dropna(), bins = 20, normed = False, alpha = 0.5)

# having the labeled data be more opaque because it is under the unlabeled data and it is easier to read this way
# This way we can look at both and see how they differ

# # plot a cumulative  histogram
# _ = plt.hist(df['time to catastrophe with labeled tubulin (s)'], bins = 100, normed = True, cumulative = True, histtype = 'step')
# _ = plt.hist(df['time to catastrophe with unlabeled tubulin (s)'].dropna(), bins = 100, normed = True, cumulative = True, histtype = 'step')

# plot a cumulative histogram like Fig 2a
_ = plt.hist(df['time to catastrophe with labeled tubulin (s)'], normed = True, cumulative = True, histtype = 'step')
_ = plt.hist(df['time to catastrophe with unlabeled tubulin (s)'].dropna(), normed = True, cumulative = True, histtype = 'step')

# Name the axes
plt.xlabel('time to catastrophe (s)')
plt.ylabel('catastrophe events')

# Add a legend
plt.legend(('labeled', 'unlabeled'), loc='upper right')
