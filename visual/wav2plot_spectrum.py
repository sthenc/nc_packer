#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav
import matplotlib as ml
import matplotlib.pyplot as plt



def plot_spectrum_array(spectrum_data):
	
	# TODO adjust this
	#vmin = 0
	#vmax = 200000000
	vmin = -125
	vmax = 0
	
	ml.rcParams['image.cmap'] = 'nipy_spectral'

	fig, axes = plt.subplots(nrows=1, ncols=1)

	
	a = axes.pcolormesh(spectrum_data.transpose(), vmin=vmin, vmax=vmax)
	axes.set_aspect('auto')

	plt.colorbar(a, orientation='horizontal')

	plt.tight_layout()
	plt.show()



def wav2spectrum(filepath):

	(sr,sig) = wav.read(filepath)

	#sigmono = sig[:, 0]
	#print (sigmono)
	
	# first frame the signals
	# 25 ms frame with 10 ms step
	# sr = 16000
	frame_len = int(0.025 * sr)
	frame_step = int(0.01 * sr)
	
	frame_data = features.sigproc.framesig(sig, frame_len, frame_step, winfunc=np.hamming)
	
	print (frame_data)
	# then compute power spectrum
	# use log power spectrum because the range of values was huge
	ret = features.sigproc.logpowspec(frame_data, frame_len)
	
	print(np.max(np.max(ret)))
	print(np.min(np.min(ret)))

	return ret


if __name__ == "__main__":
	fp = "data/clean.wav"
	
	spec = wav2spectrum(fp)
	
	plot_spectrum_array(spec)
