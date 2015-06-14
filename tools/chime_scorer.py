#!/usr/bin/python

import numpy as np

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('inset', choices=['test', 'val', 'train']) # all ? 
parser.add_argument('recog', choices=['clean', 'reverb', 'noisy', 'retrain']) # all ? 

parser.add_argument("testid", help="String to generate necessary folders etc.")   # can potentially delete data
parser.add_argument("netname", help="Input autosave file")

# -del argument - delete temporary files (computed features) ?

args = parser.parse_args()

#print (args)

rootdir = "/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/test/" + args.testid + "/"

#import shutil as sh
import os

if not os.path.exists(rootdir):
	os.makedirs(rootdir)

os.chdir(rootdir)

import logging

logging.basicConfig(filename='chime_scorer.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

logging.info("Program started")

logging.info("Arguments: " +  str(args))
