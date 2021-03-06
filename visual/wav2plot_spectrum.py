#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav
import matplotlib as ml
import matplotlib.pyplot as plt



def plot_spectrum_array(spectrum_data, savefile):
	
	#vmin = 0
	#vmax = 200000000
	vmin = -130
	vmax = 0
	
	ml.rcParams['image.cmap'] = 'nipy_spectral'
	
	fig = plt.figure()
	
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	ax.set_xlim((0,spectrum_data.shape[0]))
	ax.set_ylim((0,spectrum_data.shape[1]))

	fig.add_axes(ax)
	ax.set_aspect("equal")
	ax.pcolormesh(spectrum_data.transpose(), vmin=vmin, vmax=vmax)
	
	#plt.colorbar(orientation='horizontal')

	#plt.tight_layout()
	plt.savefig(savefile,bbox_inches='tight', dpi=300)
	


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
	
	dataroot = "data/"
	fps = [ "clean", "noise", "reverberated", "mix_m6dB" ] 
	suffix = ".wav"
	
	outdir = "figures/"
	ext = ".png"
	
	for fp in fps:
		file_name = dataroot + fp + suffix
		save_name = outdir + "spectrum_" + fp + ext
		spec = wav2spectrum(file_name)
		
		plot_spectrum_array(spec, save_name)
