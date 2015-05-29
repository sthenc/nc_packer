#!/usr/bin/python

import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

import htkmfc as hm

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Input mfcc.htk file")
parser.add_argument("-on", "--output-norm",
	help="Use output mean and stddev values instead of mean and stddevvalues computed on inputs for normalization",
	action="store_true")
args = parser.parse_args()

print (args.filename)

# parsed output of nc-standardize, run parse_means_stddevs if you need to update the values

# NOTE: if - else

if not args.output_norm :  # use values computed on input vectors in training set
	means = \
	np.array([ -1.22538000e+01,  -8.66553000e+00,   4.37193000e+00,
			-1.79456000e+01,   3.83324000e-01,  -1.54190000e+01,
			 9.03727000e-02,  -1.04591000e+00,   1.59385000e+00,
			-1.23574000e+00,  -4.91619000e+00,  -2.65313000e+00,
			 1.87613000e+01,   1.00033000e-03,   9.02196000e-03,
			-3.23978000e-03,  -3.04623000e-03,   1.25714000e-03,
			-5.17110000e-03,   4.44705000e-03,   5.00199000e-03,
			-1.70642000e-03,  -4.12547000e-03,  -1.11745000e-02,
			-1.02737000e-02,   9.56946000e-04,   1.85204000e-04,
			-1.73344000e-04,  -3.87119000e-05,   6.56798000e-04,
			-5.71323000e-05,   3.90705000e-04,  -1.91209000e-04,
			-2.45589000e-04,   2.39208000e-04,   3.14330000e-04,
			 5.09033000e-04,   3.26321000e-04,  -1.00542000e-04])
	stddevs = \
	np.array([ 10.2676   ,  13.5594   ,  14.2389   ,  14.4613   ,  14.8838   ,
			14.4155   ,  15.1032   ,  14.6793   ,  14.319    ,  13.6299   ,
			13.4591   ,  12.1276   ,   1.20224  ,   1.82959  ,   2.19346  ,
			 2.47668  ,   2.84661  ,   3.04884  ,   3.04054  ,   3.22284  ,
			 3.28088  ,   3.27445  ,   3.19905  ,   3.17187  ,   2.95972  ,
			 0.212193 ,   0.676198 ,   0.807925 ,   0.947628 ,   1.12923  ,
			 1.22298  ,   1.26538  ,   1.35223  ,   1.38832  ,   1.39287  ,
			 1.37075  ,   1.35812  ,   1.2741   ,   0.0830071])
			 
else:					# use values computed on output vectors in training set
	means = \
	np.array([ -3.23225000e+00,  -2.92348000e+00,   1.01032000e+01,
			-8.46742000e+00,  -1.36592000e+01,  -8.89385000e+00,
			-9.02748000e+00,  -2.52756000e+00,  -1.32227000e+00,
			 2.13573000e+00,  -3.30234000e+00,  -8.30571000e-01,
			 1.84567000e+01,   3.84308000e-02,  -6.19420000e-02,
			-3.91297000e-02,  -3.54161000e-02,  -2.95848000e-02,
			-4.37484000e-02,  -3.21925000e-02,  -2.00233000e-02,
			-2.33652000e-02,  -2.95121000e-02,  -2.86187000e-02,
			-1.28524000e-02,   7.99636000e-03,   1.06740000e-03,
			 1.43210000e-03,   1.72266000e-03,   3.89929000e-03,
			 3.96768000e-03,   4.28519000e-03,   1.37717000e-03,
			 1.62659000e-03,  -2.56732000e-04,   2.08233000e-04,
			 1.86665000e-03,   9.58680000e-04,  -3.14592000e-03])
	stddevs = \
	np.array([ 20.1514  ,  16.9231  ,  18.7397  ,  20.4217  ,  21.1932  ,
			17.9403  ,  19.6735  ,  18.1267  ,  18.1856  ,  15.6424  ,
			16.2007  ,  13.1955  ,   2.2268  ,   4.32275 ,   4.02244 ,
			 4.01032 ,   4.60773 ,   4.90577 ,   4.41624 ,   4.5844  ,
			 4.4641  ,   4.20475 ,   3.85852 ,   3.80428 ,   3.37943 ,
			 0.487057,   1.6352  ,   1.61938 ,   1.54493 ,   1.81739 ,
			 1.94619 ,   1.84266 ,   1.89011 ,   1.86456 ,   1.7389  ,
			 1.63711 ,   1.58745 ,   1.43842 ,   0.181184])





io_klasa = hm.HTKFeat_read(args.filename)

mfcc_data = io_klasa.getall()

# normalize

mfcc_data = (mfcc_data - means) / stddevs

print(mfcc_data)
print(mfcc_data.shape)

# plot the mfcc features from original chime file and compare to the ones in the .nc database
ml.rcParams['image.cmap'] = 'nipy_spectral'

fig, axes = plt.subplots(nrows=1, ncols=1)


# +- 6 for normalized, +- 60 for non-normalized
vmin = -6
vmax =  6	

a = axes.pcolormesh(mfcc_data.transpose(), vmin=vmin, vmax=vmax)
axes.set_aspect('equal')

plt.colorbar(a, orientation='horizontal')

plt.tight_layout()
plt.show()
