#!/usr/bin/python

import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

import features
import scipy.io.wavfile as wav


datadir = '/mnt/data/Fer/diplomski/nc_packer/test_data/PCCdata16kHz/devel/isolated/'

cleandir = 'clean/'

lilnoise = 'm3dB/'

fajl = 's1_bgaa9a.wav'

# Input #0, wav, from 's1_bgaa9a.wav':
#   Duration: 00:00:01.25, bitrate: 512 kb/s
#     Stream #0.0: Audio: pcm_s16le, 16000 Hz, stereo, s16, 512 kb/s


(sr,sig1) = wav.read(datadir + cleandir + fajl)

sig1mono = sig1[:, 0]
print (sig1mono)

mfcc_clean = features.mfcc(sig1mono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=78)

print (mfcc_clean)

(sr,sig2) = wav.read(datadir + lilnoise + fajl)

sig2mono = sig2[:, 0]
print (sig2mono)

mfcc_noisy = features.mfcc(sig2mono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=78)

print (mfcc_noisy)


ml.rcParams['image.cmap'] = 'nipy_spectral'

fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(211)
plt.pcolormesh(mfcc_clean.transpose())
ax.set_aspect('equal')

ax = fig.add_subplot(212)
plt.pcolormesh(mfcc_noisy.transpose())
ax.set_aspect('equal')

# add colorbar 

#cax = fig.add_axes([0.85, 0.1, 0.1, 0.7])
fig.subplots_adjust(right=0.8)
cax = fig.add_axes([0, 0.1, 1, 0.8], aspect='auto', frameon=False, xticks=[], yticks=[])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical', ax=cax)

#plt.tight_layout()
plt.show()
