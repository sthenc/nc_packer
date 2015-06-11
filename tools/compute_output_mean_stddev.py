#!/usr/bin/python

import numpy as np
#import matplotlib as ml
#import matplotlib.pyplot as plt

# computes means and stddev for every mfcc bin for all the test files
# in the entire development test set


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("foldername", help="foldername for tree with .mfcc features")
parser.add_argument("savename", help="file to save means and stddevs to")
args = parser.parse_args()

#mypath = '/mnt/data/Fer/diplomski/nc_packer/tmp_test/'
#mypath = '/mnt/data/Fer/diplomski/CHiME2/eval_tools_grid/features/mfcc/test_raw/'
mypath = args.foldername #'/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/test/test2/output-test-norm/'
extension = 'mfcc'

from os import listdir
from os.path import isfile, join
import os

print (mypath)

dirs = [ x for x in os.listdir(mypath) if os.path.isdir(mypath + x) ]
print(dirs)

onlyfiles = []

for d in dirs:
	onlyfiles.extend( [d + "/" + f for f in os.listdir(mypath + d) if f.split('.')[1] == extension ] ) 

print(onlyfiles)


NC = 39 # number of ceptral coefficients

means = np.zeros(NC)
stddevs = np.zeros(NC)

N = 0

import htkmfc as hm


for f in onlyfiles:
	#f = onlyfiles[]
	
	io_klasa = hm.HTKFeat_read(mypath + f)

	mfccs = io_klasa.getall()


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

import json

savefile = open(args.savename, "w")

meanslist = list(means)
stddevslist = list(stddevs)
json.dump((meanslist, stddevslist), savefile)


savefile.close()
