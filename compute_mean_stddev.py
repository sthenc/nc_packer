#!/usr/bin/python3

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

print(onlyfiles)
