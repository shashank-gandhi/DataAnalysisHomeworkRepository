# Our numerical workhorses
import numpy as np
import pandas as pd
import scipy.signal
import scipy.special
import scipy.stats as st

# Import plotting tools
import matplotlib.pyplot as plt
import seaborn as sns
import corner

# Justin's favorite settings
rc = {'lines.linewidth': 2,
      'axes.labelsize': 18,
      'axes.titlesize': 18,
      'axes.facecolor': 'DFDFE5'}
sns.set_context('notebook', rc=rc)
sns.set_style('darkgrid', rc=rc)

df = pd.read_csv('./data/H930start2filt.txt', comment = '#', sep = '\t', names=['t (ms)', 'V (µV)'], header = None)

# change time to seconds
df['t (ms)'] /= 1000
df = df.rename(columns= {'t (ms)' : 't (s)'})

# plot our data to look at it
# plt.plot(df['t (s)'], df['V (µV)'], zorder = 2)


# now we want to find local minima and maximas using what we discussed in class
# we can define a threshold
thresh = -120
V = df['V (µV)'].values
down = np.where(np.logical_and(V[:-1] > thresh, V[1:] < thresh))[0]
up = np.where(np.logical_and(V[:-1] < thresh, V[1:] > thresh))[0]

# now that i have a down and up value to find the minimum i can assume to take the average of the down and up value
local_min = (down + up) / 2

# now i want to set windows around these local minimums
time_window_L = 0.0005
time_window_R = 0.002

inter_sample_time = df['t (s)'][1] - df['t (s)'][0]
sampling_frequency = 1 / inter_sample_time

left_window = int(time_window_L * sampling_frequency)
right_window = int(time_window_R * sampling_frequency)

df_min = pd.DataFrame(columns =['t (s)', 'V (µV)', 'spike'])
i = 0
for i in range (len(down)):
    t_min = df['t (s)'][down[i] - left_window:up[i] + right_window]
    V_min = df['V (µV)'][down[i] - left_window:up[i] + right_window]
    data={'t (s)': t_min, 'V (µV)': V_min, 'spike': int((down[i] + up[i]) / 2) * np.ones_like(t_min, dtype=int)}
    df_data = pd.DataFrame(data)
    df_min = pd.concat((df_min, df_data))
    i += 1

# just checking the window size
# for spike in df_min['spike'].unique():
#     inds = df_min['spike'] == spike
#     plt.plot(np.arange(inds.sum()), df_min['V (µV)'][inds], lw=1, alpha=0.05, color='black')


# now i want to be able to differentiate between the two different spikes
# there are 2 types of spikes
# type a does not overshoots when it comes up
# type b overshoots when it comes up
# Let's do something similar to what we did to find the spikes

# let's define a thresh for high peaks
thresh_high = 50
V_high = df_min['V (µV)'].values

# let's find our peaks
down_high = np.where(np.logical_and(V_high[:-1] > thresh_high, V_high[1:] < thresh_high))[0]
up_high = np.where(np.logical_and(V_high[:-1] < thresh_high, V_high[1:] > thresh_high))[0]

# i want to group by spikes

# let's set windows same way as before
df_max = pd.DataFrame(columns =['t (s)', 'V (µV)', 'spike'])
i = 0
for i in range (len(down_high)):
    t_max = df['t (s)'][down_high[i] - left_window:up_high[i] + right_window]
    V_max = df['V (µV)'][down_high[i] - left_window:up_high[i] + right_window]
    data={'t (s)': t_max, 'V (µV)': V_max, 'spike': int((down_high[i] + up_high[i]) / 2) * np.ones_like(t_max, dtype=int)}
    df_data_max = pd.DataFrame(data)
    df_max = pd.concat((df_max, df_data_max))
    i += 1

for spike in df_max['spike'].unique():
    inds = df_max['spike'] == spike
    plt.plot(np.arange(inds.sum()), df_max['V (µV)'][inds], lw=1, alpha=0.05, color='black')



plt.draw()
plt.show()

