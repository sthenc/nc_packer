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

	for i in range(0, NC):
		means[i] += sum(mfccs[0:lilN, i])


	N = N + lilN

print(N)
print(means)

means = means/N

from pprint import pprint
pprint(means)
	

for f in onlyfiles:
#f = onlyfiles[0]

	mfccs = wav2mfcc(mypath + f)

	sh = mfccs.shape

	lilN = sh[0]

	for i in range(0, NC):
		stddevs[i] += sum(mfccs[0:lilN, i] - means[i])**2

#print(stddevs)

stddevs /= N
print(stddevs)

from math import sqrt

for i in range(0, NC):
	stddevs[i] = sqrt(stddevs[i])
	
pprint(stddevs)
