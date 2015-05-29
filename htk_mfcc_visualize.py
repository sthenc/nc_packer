#!/usr/bin/python

import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

import htkmfc as hm

io_klasa = hm.HTKFeat_read('bbaf2n.wav.mfcc.htk')

mfcc_data = io_klasa.getall()


print(mfcc_data)
print(mfcc_data.shape)

# plot the mfcc features from original chime file and compare to the ones in the .nc database
ml.rcParams['image.cmap'] = 'nipy_spectral'

fig, axes = plt.subplots(nrows=1, ncols=1)


# +- 6 for normalized, +- 60 for non-normalized
vmin = -60
vmax = 60	

a = axes.pcolormesh(mfcc_data.transpose(), vmin=vmin, vmax=vmax)
axes.set_aspect('equal')

plt.colorbar(a, orientation='vertical')

plt.tight_layout()
plt.show()
