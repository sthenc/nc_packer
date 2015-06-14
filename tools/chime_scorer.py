#!/usr/bin/python

import numpy as np
import shutil as sh
import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("testid", help="String to generate necessary folders etc.")   # can potentially delete data
parser.add_argument("netname", help="Input autosave file")
inset = parser.add_mutually_exclusive_group()
inset.add_argument("-val", "--validate",
	help="Score network on validation set",
	action="store_true")
inset.add_argument("-tst", "--test",
	help="Score network on test set",
	action="store_true")
inset.add_argument("-trn", "--train",
	help="Score network on training set",
	action="store_true")
recog = parser.add_mutually_exclusive_group()
recog.add_argument("-cl", "--clean",
	help="Score network output using the clean model",
	action="store_true")
recog.add_argument("-ns", "--noisy",
	help="Score network output using the noisy model",
	action="store_true")
recog.add_argument("-rv", "--reverberated",
	help="Score network output using the reverberated model",
	action="store_true")
recog.add_argument("-rt", "--retrain",
	help="Score network output using a model retrained on training data",
	action="store_true")


# -all argument - compute all possible combinations for selected network
# -del argument - delete temporary files (computed features)

args = parser.parse_args()

print (args)
