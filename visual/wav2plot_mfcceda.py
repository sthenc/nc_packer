#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav
import matplotlib as ml
import matplotlib.pyplot as plt
import htkmfc as hm

def plot_mfcceda_array(data_name, savefile):
	
	# TODO adjust this
	#vmin = 0
	#vmax = 200000000
	
	io_klasa = hm.HTKFeat_read(data_name)

	data = io_klasa.getall()
	
	vmin = -60
	vmax = 60
	
	ml.rcParams['image.cmap'] = 'nipy_spectral'
		
	fig = plt.figure()

	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	ax.set_xlim((0,data.shape[0]))
	ax.set_ylim((0,data.shape[1]))

	fig.add_axes(ax)
	ax.set_aspect("equal")
	ax.pcolormesh(data.transpose(), vmin=vmin, vmax=vmax)
	
	#plt.colorbar(orientation='horizontal')

	#plt.tight_layout()
	plt.savefig(savefile,bbox_inches='tight')

import os

def wav2mfcceda(filepathin, filepathout):

	# call openSMILE 
	
	command = "SMILExtract -C ../MFCC12_E_D_A.conf -logfile smile.log -noconsoleoutput 1 -appendLogfile 1 "
	
	command = command + " -I " + filepathin + " -O " + filepathout
	
	return os.system(command)
	


if __name__ == "__main__":
	
	dataroot = "data/"
	fps = [ "clean", "noise", "reverberated", "mix_m6dB" ] 
	suffix = ".wav"
	
	mfccdir = "data/mfcc/"
	mfext = ".mfcc"
	
	picdir = "figures/"
	pext = ".png"
	
	for fp in fps:
		file_name = dataroot + fp + suffix
		mfcc_name = mfccdir + fp + mfext
		save_name = picdir + "mfcceda_" + fp + pext
		
		spec = wav2mfcceda(file_name, mfcc_name)
		
		plot_mfcceda_array(mfcc_name, save_name)
