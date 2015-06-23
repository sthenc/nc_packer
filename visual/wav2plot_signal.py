#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav
import matplotlib as ml
import matplotlib.pyplot as plt



def plot_signal(data, savefile):
	
	#vmin = 0
	#vmax = 200000000
	#vmin = -130
	#vmax = 0
	
	ml.rcParams['image.cmap'] = 'nipy_spectral'
	
	
	plt.plot(data)
	fig = plt.figure()
	
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
    
	fig.add_axes(ax)
	ax.plot(data)
	
	plt.savefig(savefile,bbox_inches='tight', dpi=300)
	plt.clf()


def wav2signal(filepath):

	(sr,sig) = wav.read(filepath)
   
	return sig


if __name__ == "__main__":
	
	dataroot = "data/"
	fps = [ "clean", "noise", "reverberated", "mix_m6dB" ] 
	suffix = ".wav"
	
	outdir = "figures/"
	ext = ".png"
	
	for fp in fps:
		file_name = dataroot + fp + suffix
		save_name = outdir + "signal_" + fp + ext
		spec = wav2signal(file_name)
		
		plot_signal(spec, save_name)
