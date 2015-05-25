#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav

def wav2mfcc(filepath):

	(sr,sig) = wav.read(filepath)

	sigmono = sig[:, 0]
	#print (sigmono)


	sig_mfcc= features.mfcc(sigmono,sr, winlen=0.01, winstep=0.01, numcep=12, nfilt=22)
	#sig_mfcc= features.mfcc(sigmono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=78)

	#sig_mfcc= features.mfcc(sigmono,sr, winlen=0.01, winstep=0.01, numcep=39, nfilt=50)
	
	
	ret = np.zeros((sig_mfcc.shape[0], 39))
	
	ret[0:sig_mfcc.shape[0], 1:13 ] = sig_mfcc
	return ret
