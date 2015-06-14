#!/usr/bin/python

import numpy as np

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('inset', choices=['test', 'val', 'train', 'all']) 
parser.add_argument('recog', choices=['clean', 'reverb', 'noisy', 'retrain', 'all']) 
phase_group = ArgumentParser.add_mutually_exclusive_group(required = False)

phase_group.add_argument("-gen", "--just-generate",
	help="Only generate features",
	action="store_true")
	
phase_group.add_argument("-tst", "--just-test",
	help="Only generate features",
	action="store_true")
	
parser.add_argument("-od", 

parser.add_argument("testid", help="String to generate necessary folders etc.")   # can potentially delete data
parser.add_argument("netname", help="Input autosave file")

parser.add_argument("-del", "--delete",
	help="Delete generated features to save space",
	action="store_true")

args = parser.parse_args()

#print (args)

rootdir = "/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/test/" + args.testid + "/"

import shutil as sh
import os

if not os.path.exists(rootdir):
	os.makedirs(rootdir)

os.chdir(rootdir)

import logging

logging.basicConfig(filename='chime_scorer.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

logging.info("Program started")

logging.info("Arguments: " +  str(args))


# feature generate phase

testfeat = "output_test/"
valfeat = "output_val/"
trainfeat = "output_train/"

testnc = "../../test_reverb_norm.nc"
valnc = "../../val_reverb_norm.nc"
trainnc = "../../val_reverb_norm.nc"

for f in [testfeat, valfeat, trainfeat]:
	if not os.path.exists(rootdir + f):
		os.makedirs(rootdir + f)
		logging.info("Created " + rootdir + f)

for f in [testnc, valnc, trainnc]:
	if not os.path.isfile(rootdir + f):
		logging.error("File doesn't exist: " + rootdir + f)
		print("File doesn't exist: " + rootdir + f)
		exit()


if args.inset == "test"  or args.inset == "all" :
	print("test")
	
	if os.path.exists(rootdir + testfeat):
		sh.rmtree(rootdir + testfeat)
	
	

# feature score phase


# finish: save results to .ods file or someting
