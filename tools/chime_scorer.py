#!/usr/bin/python

import numpy as np
import shutil as sh
import os

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('inset', choices=['test', 'val', 'train']) # all ? 
parser.add_argument('recog', choices=['clean', 'reverb', 'noisy', 'retrain']) # all ? 

parser.add_argument("testid", help="String to generate necessary folders etc.")   # can potentially delete data
parser.add_argument("netname", help="Input autosave file")

# -del argument - delete temporary files (computed features) ?

args = parser.parse_args()

print (args)
