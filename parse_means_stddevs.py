#!/usr/bin/python3

import numpy as np

from pprint import pprint	

# parse output of nc-standardize

filename = 'train_means_stddevs.txt'

fajl = open(filename, 'r')

lines = fajl.readlines()

lines = lines[3:81]

#pprint(lines)


inmeans    = np.zeros(39)
instddevs  = np.zeros(39)
outmeans   = np.zeros(39)
outstddevs = np.zeros(39)

for i in range(0, 39):
	tokens = lines[i].split(' ')
	
	#print(tokens)
	
	inmeans  [i] = float(tokens[5])
	instddevs[i] = float(tokens[7])
	
print("inmeans = \\\nnp.", end="")
pprint(inmeans)
print("instddevs = \\\nnp.", end="")
pprint(instddevs)

for i in range(39, 78):
	tokens = lines[i].split(' ')
	
	#print(tokens)
	
	outmeans  [i - 39] = float(tokens[5])
	outstddevs[i - 39] = float(tokens[7])
	
print("outmeans = \\\nnp.", end="")
pprint(outmeans)
print("outstddevs = \\\nnp.", end="")
pprint(outstddevs)
