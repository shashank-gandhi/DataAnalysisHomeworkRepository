# 1.3

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

# read the csv into a dataframe
df = pd.read_csv('gardner_et_al_2011_time_to_catastrophe_dic.csv', comment = '#')

# This data is not tidy because each row is not an observation

# splice the data tables

df_labeled = df['time to catastrophe with labeled tubulin (s)']
df_unlabeled = df['time to catastrophe with unlabeled tubulin (s)']


# Drop all NaN values
df_unlabeled_clean = df['time to catastrophe with unlabeled tubulin (s)'].dropna()

#plot the two data sets

#_ = plt.hist(df_labeled, bins = 30, normed = False)
#_ = plt.hist(df_unlabeled_clean, bins = 30, normed = False, alpha = 0.5, color="red")

# having the labeled data be more opaque because it is under the unlabeled data and it is easier to read this way
# This way we can look at both and see how they differ


"""

#plot a cumulative  histogram
_ = plt.hist(df_labeled, bins = 100, normed=1, cumulative = True, histtype = 'stepfilled', linewidth=2.0)
_ = plt.hist(df_unlabeled_clean, normed=1, bins = 100, cumulative = True, histtype = 'stepfilled', linewidth=2.0, alpha=0.4)

"""


# plot a cumulative histogram like Fig 2a

#get bin size
timepoints = np.arange( np.min (df_unlabeled_clean), np.max(df_unlabeled_clean) +30, 30  )

sorted_df_labeled = np.sort(df_labeled)
sorted_df_unlabeled = np.sort(df_unlabeled_clean)

empty_array_labeled = np.zeros( len(timepoints))
empty_array_unlabeled = np.zeros ( len(timepoints) )

for i in range( len(timepoints) ):
    empty_array_labeled[i] = np.sum (sorted_df_labeled < timepoints[i])
    empty_array_unlabeled [i] = np.sum (sorted_df_unlabeled < timepoints[i])

normalized_labeled = empty_array_labeled / np.max( empty_array_labeled)

normalized_unlabeled = empty_array_unlabeled / np.max (empty_array_unlabeled)

_ = plt.plot(timepoints, normalized_labeled , marker="o", linestyle = "None")
_= plt.plot( timepoints, normalized_unlabeled, marker = "o", linestyle ="None", color="red", alpha = 0.5)


# # Name the axes
plt.xlabel('Time to Catastrophe (s)')
plt.ylabel('Cumulative Probability Distribution')
plt.ylim(0,1.1)
# # Add a legend
plt.legend(('labeled', 'unlabeled'), loc='lower right', prop={"size":15})

plt.draw()
plt.show()
