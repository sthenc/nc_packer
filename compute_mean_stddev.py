#!/usr/bin/python

import numpy as np
#import matplotlib as ml
#import matplotlib.pyplot as plt

import features
import scipy.io.wavfile as wav

# computes means and stddev for every mfcc bin for all the test files
# in the entire development test set

mypath = '/mnt/data/Fer/diplomski/nc_packer/test_data/PCCdata16kHz/devel/isolated/clean/'

from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

print('#files ' + str(len(onlyfiles)))

from wav2mfcc import wav2mfcc

NC = 39 # number of ceptral coefficients

means = np.zeros(NC)
stddevs = np.zeros(NC)

N = 0

for f in onlyfiles:
	#f = onlyfiles[0]
	mfccs = wav2mfcc(mypath + f)


	#print(f)
	sh = mfccs.shape
	#print(sh)

	lilN = sh[0]

	for j in range (0, lilN):
		N += 1
		for i in range(0, NC):
			x = mfccs[j][i]
			delta = x - means[i]
			means[i] += delta / N
			stddevs[i] += delta * (x - means[i])
	
from pprint import pprint	

print(N)
print(means)

pprint(means)
	
stddevs /= N - 1

from math import sqrt

delta = 0.0000001

for i in range(0, NC):
	stddevs[i] = sqrt(stddevs[i])
	if abs(stddevs[i] - 0.0) < delta:
		stddevs[i] = 1.0

pprint(stddevs)
