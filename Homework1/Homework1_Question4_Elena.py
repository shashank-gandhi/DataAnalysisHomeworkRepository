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
<<<<<<< HEAD
=======

#geomag_df = df[df['TaxonOrig'] == 'Geospiza magnirostris']
#
#geomag_Gnov_Twr = geomag_df[geomag_df['IslandID'] == 'Gnov_Twr'] 
#geomag_Pnt_Abng = geomag_df[geomag_df['IslandID'] == 'Pnt_Abng'] 
#geomag_Wlf_Wnm = geomag_df[geomag_df['IslandID'] == 'Wlf_Wnm']
#
#geomag_three_islands = pd.concat([geomag_Gnov_Twr, geomag_Pnt_Abng, 
#                                  geomag_Wlf_Wnm])
#
#sns.stripplot(x=geomag_three_islands['IslandID'], 
#              y=geomag_three_islands['UBeakL'], data=df, jitter=True,
#              alpha=0.6) 
#plt.ylabel('Upper Beak Length (mm)')
#plt.xlabel('Island ID')  
#plt.title('Upper beak length of Geospiza magnirostris') 

ful_df = df[df['TaxonOrig'] == 'Geospiza fuliginosa']

ful_Mrch_Bndl = ful_df[ful_df['IslandID'] == 'Mrch_Bndl'] 
ful_Isa_Alb = ful_df[ful_df['IslandID'] == 'Isa_Alb'] 
ful_Flor_Chrl = ful_df[ful_df['IslandID'] == 'Flor_Chrl']
ful_Balt_SS = ful_df[ful_df['IslandID'] == 'Balt_SS']

ful_islands = pd.concat([ful_Mrch_Bndl, ful_Isa_Alb, ful_Flor_Chrl, 
                         ful_Balt_SS])
                         
sca_df = df[df['TaxonOrig'] == 'Geospiza scandens']

sca_Mrch_Bndl = sca_df[sca_df['IslandID'] == 'Mrch_Bndl'] 
sca_Isa_Alb = sca_df[sca_df['IslandID'] == 'Isa_Alb'] 
sca_Flor_Chrl = sca_df[sca_df['IslandID'] == 'Flor_Chrl']
sca_Balt_SS = sca_df[sca_df['IslandID'] == 'Balt_SS']

sca_islands = pd.concat([sca_Mrch_Bndl, sca_Isa_Alb, sca_Flor_Chrl, 
                         sca_Balt_SS])
                         
sns.stripplot(x=ful_islands['IslandID'], 
              y=ful_islands['UBeakL'], data=df, jitter=True, color='Blue',
              alpha=0.6) 
sns.stripplot(x=sca_islands['IslandID'], 
              y=sca_islands['UBeakL'], data=df, jitter=True, color='Red',
              alpha=0.6)               
plt.ylabel('Upper Beak Length (mm)')
plt.xlabel('Island ID')             

plt.draw()
plt.show()
                               

>>>>>>> 018fcb7facd0b0171a0d3d780feee2870ff5a326
