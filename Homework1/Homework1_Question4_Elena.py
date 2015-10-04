# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# JB's favorite Seaborn settings for notebooks
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18,
    'axes.facecolor': 'DFDFE5'}
sns.set_context('paper', rc=rc)

plt.close('all')

df = pd.read_csv('./data/morphLack.TAB', delimiter='\t')
