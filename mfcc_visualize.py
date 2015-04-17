#!/usr/bin/python

import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

import features
import scipy.io.wavfile as wav


#if __name__ == "__main__":

datadir = '/mnt/data/Fer/diplomski/nc_packer/test_data/PCCdata16kHz/devel/isolated/'

cleandir = 'clean/'

lilnoise = 'm3dB/'

fajl = 's1_bgaa9a.wav'

# Input #0, wav, from 's1_bgaa9a.wav':
#   Duration: 00:00:01.25, bitrate: 512 kb/s
#     Stream #0.0: Audio: pcm_s16le, 16000 Hz, stereo, s16, 512 kb/s


# compute my mfcc features for this file

(sr,sig1) = wav.read(datadir + cleandir + fajl)

sig1mono = sig1[:, 0]
print (sig1mono)

mfcc_clean= features.mfcc(sig1mono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=78)

print (mfcc_clean)

(sr,sig2) = wav.read(datadir + lilnoise + fajl)

sig2mono = sig2[:, 0]
print (sig2mono)

mfcc_noisy= features.mfcc(sig2mono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=78)


print (mfcc_noisy)


# mine .nc file

import netCDF4

# ds = netCDF4.Dataset('./train_1_speaker.nc')
ds = netCDF4.Dataset('./val_1_speaker.nc')

#print(ds)

dslen = ds.variables['seqLengths']
dsin  = ds.variables['inputs']
dsout = ds.variables['targetPatterns'] 

print(dslen[:])
sz = dslen[0]

ds_mfcc_clean = dsin [0:sz, :]
ds_mfcc_noisy = dsout[0:sz, :]

# plot the mfcc features from original chime file and compare to the ones in the .nc database
ml.rcParams['image.cmap'] = 'nipy_spectral'

fig, axes = plt.subplots(nrows=4, ncols=1)

vmin = min(min(np.amin(mfcc_clean), np.amin(mfcc_noisy)), min(np.amin(ds_mfcc_clean), np.amin(ds_mfcc_noisy)))
vmax = max(max(np.amax(mfcc_clean), np.amax(mfcc_noisy)), max(np.amax(ds_mfcc_clean), np.amax(ds_mfcc_noisy)))

print(min(np.amin(mfcc_clean), np.amin(mfcc_noisy)))
print(max(np.amax(mfcc_clean), np.amax(mfcc_noisy)))

axes[0].pcolormesh(mfcc_clean.transpose(), vmin=vmin, vmax=vmax)
axes[0].set_aspect('equal')

axes[1].pcolormesh(mfcc_noisy.transpose(), vmin=vmin, vmax=vmax)
axes[1].set_aspect('equal')

axes[2].pcolormesh(ds_mfcc_clean.transpose(), vmin=vmin, vmax=vmax)
axes[2].set_aspect('equal')

a= axes[3].pcolormesh(ds_mfcc_noisy.transpose(), vmin=vmin, vmax=vmax)
axes[3].set_aspect('equal')


# add colorbar 

fig.subplots_adjust(right=0.8)
cax = fig.add_axes([0.80, 0.05, 0.1, 0.9], aspect='auto', frameon=False, xticks=[], yticks=[])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(a, orientation='vertical', ax=cax, aspect=60)

plt.tight_layout()
plt.show()
