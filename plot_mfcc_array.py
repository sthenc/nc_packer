import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

def plot_mfcc_array(mfcc_data):
	
	vmin = -60
	vmax =  60
	
	ml.rcParams['image.cmap'] = 'nipy_spectral'

	fig, axes = plt.subplots(nrows=1, ncols=1)

	
	a = axes.pcolormesh(mfcc_data.transpose(), vmin=vmin, vmax=vmax)
	axes.set_aspect('equal')

	plt.colorbar(a, orientation='horizontal')

	plt.tight_layout()
	plt.show()


