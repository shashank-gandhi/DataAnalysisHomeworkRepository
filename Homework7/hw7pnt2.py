import glob
import os
import warnings

# Our numerical workhorses
import numpy as np
import pandas as pd
import scipy.signal
import scipy.stats as st

# BE/Bi 103 utilities
import bebi103

# Image processing tools
import skimage
import skimage.io

# Import plotting tools
import matplotlib.pyplot as plt
import seaborn as sns

# Justin's favorite settings
rc = {'lines.linewidth': 2,
      'axes.labelsize': 18,
      'axes.titlesize': 18,
      'axes.facecolor': 'DFDFE5'}
sns.set_context('notebook', rc=rc)
sns.set_style('darkgrid', rc=rc)


fname = './data/goehring_FRAP_data/PH_138_A.tif'

vert = (16.435483870967744, 10.274193548387103)
b = (vert[0], vert[1] + 40)
c = (vert[0] + 40, vert[1])
d = (vert[0] + 40, vert[1] + 40)

verts = np.array([vert, b, c, d])




# use justin's roi utility
roi, roi_bbox, roi_box = bebi103.verts_to_roi(verts, 128, 128)


img_num = 149

# define a function roi
def load_roi(fname, img_num=0, roi_bbox = None):
    '''
    define a roi area
    '''
    out = np.empty(149)
    print ("running function")
   # print (out)

   # for i in range(img_num):

       # print (i)
    out = skimage.io.imread(fname)[img_num][roi_bbox]
#        print (out)
    return out

x = np.empty(149)

for i in range(149):
    img_num = i
    x[i] = load_roi(fname,roi_bbox = roi_bbox)

#ic = skimage.io.ImageCollection(fname, conserve_memory = True, load_func = load_roi, roi_bbox = roi_bbox)

# define a timeframe
fps = 5.32
t = np.arange(0, len(ic))/fps

intensity = np.empty(len(t))
# measure the intensity
#for i in range(len(ic)):
 #   intensity[i] = ic[i][roi_box].mean()


