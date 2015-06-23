#!/usr/bin/python

import numpy as np
import features
import scipy.io.wavfile as wav
import matplotlib as ml
import matplotlib.pyplot as plt
import htkmfc as hm

def plot_mfcceda_array(data_name, savefile, norm=False):
	
	# TODO adjust this
	#vmin = 0
	#vmax = 200000000
	
	print(data_name, savefile)
	
	io_klasa = hm.HTKFeat_read(data_name)

	data = io_klasa.getall()
	
	if not norm:
		vmin = -60
		vmax = 60
	else:
		vmin = -6
		vmax = 6
	
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
	
from means_file import *

def normalize_originaltrain(infile, outfile):
	io_klasa = hm.HTKFeat_read(infile)

	data = io_klasa.getall()
	
	data_norm = (data - train_means) / train_stddevs
	
	io_klasa = hm.HTKFeat_write(outfile, veclen = 39, sampPeriod = 100000, paramKind = 2886)  # 2886 MFCC_E_D_A_Z, 838 MFCC_E_D_A
	
	io_klasa.writeall(data_norm)
	io_klasa.close()
	
	return 0 
	
def enhance(infile, outfile):
	
	return os.system("cp " + infile + " " + outfile)

def normalize_tohtk(infile, outfile):
	io_klasa = hm.HTKFeat_read(infile)

	data = io_klasa.getall()
	
	new_means = enh_means - htk_means
	new_stddevs  = enh_stddevs / htk_stddevs
	
	data_norm = (data - new_means) / new_stddevs
	
	io_klasa = hm.HTKFeat_write(outfile, veclen = 39, sampPeriod = 100000, paramKind = 2886)  # 2886 MFCC_E_D_A_Z, 838 MFCC_E_D_A
	
	io_klasa.writeall(data_norm)
	io_klasa.close()
	
	return 0 
	
def denormalize_trainoutput(infile, outfile):
	io_klasa = hm.HTKFeat_read(infile)

	data = io_klasa.getall()
	
	data_norm = (data * enh_stddevs) + enh_means 
	
	io_klasa = hm.HTKFeat_write(outfile, veclen = 39, sampPeriod = 100000, paramKind = 2886)  # 2886 MFCC_E_D_A_Z, 838 MFCC_E_D_A
	
	io_klasa.writeall(data_norm)
	io_klasa.close()
	
	return 0 

if __name__ == "__main__":
	
	netroot = "/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/test/test15/"
	
	netname = "autosave_run10_epoch197.autosave"
	
	dataroot = "data/"
	fps = [ "clean", "noise", "reverberated", "mix_m6dB" ] 
	suffix = ".wav"
	
	mfccdir = "data/mfcc/"
	mfccdir2 = "data/mfcc/generated/"
	mfext = ".mfcc"
	
	picdir = "figures/"
	pext = ".png"
	
	for fp in fps:
		file_name = dataroot + fp + suffix
		mfcc_name = mfccdir + fp + mfext
		save_name = picdir + "mfcceda_" + fp + pext
		
		mfcc_norm = mfccdir2 + fp + "_N" + mfext
		save_norm = picdir + "mfccedaN_" + fp + pext
		
		mfcc_enhnorm = mfccdir2 + fp + "_NE" + mfext
		save_enhnorm = picdir + "mfccedaNE_" + fp + pext
		
		mfcc_enhnormhtk = mfccdir2 + fp + "_NEH" + mfext
		save_enhnormhtk = picdir + "mfccedaNEH_" + fp + pext
		
		mfcc_enhdenorm = mfccdir2 + fp + "_DE" + mfext
		save_enhdenorm = picdir + "mfccedaDE_" + fp + pext
		
		wav2mfcceda(file_name, mfcc_name)
		plot_mfcceda_array(mfcc_name, save_name)
		
		normalize_originaltrain(mfcc_name, mfcc_norm)
		plot_mfcceda_array(mfcc_norm, save_norm, norm=True)
		
		enhance(mfcc_norm, mfcc_enhnorm)
		plot_mfcceda_array(mfcc_enhnorm, save_enhnorm, norm=True)
		
		normalize_tohtk(mfcc_enhnorm, mfcc_enhnormhtk)
		plot_mfcceda_array(mfcc_enhnormhtk, save_enhnormhtk, norm=True)
		
		denormalize_trainoutput(mfcc_enhnorm, mfcc_enhdenorm)
		plot_mfcceda_array(mfcc_enhdenorm, save_enhdenorm)
		
