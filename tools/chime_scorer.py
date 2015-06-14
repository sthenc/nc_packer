#!/usr/bin/python

import numpy as np

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('inset', choices=['test', 'val', 'train', 'all']) 
parser.add_argument('recog', choices=['clean', 'reverb', 'noisy', 'retrain', 'all']) 
phase_group = parser.add_mutually_exclusive_group(required = False)

phase_group.add_argument("-gen", "--just-generate",
	help="Only generate features",
	action="store_true")
	
phase_group.add_argument("-tst", "--just-test",
	help="Only generate features",
	action="store_true")
	
parser.add_argument("-cd", "--cuda",
	help="Enable cuda",
	action="store_true")

parser.add_argument("testid", help="String to generate necessary folders etc.")   # can potentially delete data
parser.add_argument("netname", help="Input autosave file")

parser.add_argument("-del", "--delete",
	help="Delete generated features to save space",
	action="store_true")

args = parser.parse_args()

#print (args)

# create and change to test directory
rootdir = "/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/test/" + args.testid + "/"

import shutil as sh
import os

if not os.path.exists(rootdir):
	os.makedirs(rootdir)

os.chdir(rootdir)


# setup logging
import logging

logging.basicConfig(filename='chime_scorer.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

logging.info("=" * 20 + "Program started" + "=" * 20)

logging.info("Arguments: " +  str(args))

# copy selected network file to test directory

import subprocess as sb

netname = os.path.basename(args.netname)

#netname = netname.split('.')[0] + ".json"

print(netname)

try:
	#print(["cp", args.netname, rootdir])
	tmp_output = sb.check_output(["cp", args.netname, rootdir], stderr=sb.STDOUT, universal_newlines=True)
	
except sb.CalledProcessError as exc:                                                                                                   
    logging.error("Invalid netname. returncode: " + str(exc.returncode) + " output: " + str(exc.output))
    print("Invalid netname")
    exit()
    
else:                                                                                                   
    logging.info("Copy netname: \n{}\n".format(tmp_output))         


# feature generate phase

testfeat  = "output_test/"
valfeat   = "output_val/"
trainfeat = "output_train/"

testfeatnorm  = "output_norm_test/"
valfeatnorm   = "output_norm_val/"
trainfeatnorm = "output_norm_train/"


#testnc = "../../test_reverb_norm.nc"
#valnc = "../../val_reverb_norm.nc"
#trainnc = "../../val_reverb_norm.nc"
testnc = valnc = trainnc = "../../dev2.nc"

for f in [testfeat, valfeat, trainfeat]:
	if not os.path.exists(rootdir + f):
		os.makedirs(rootdir + f)
		logging.info("Created " + rootdir + f)

for f in [testnc, valnc, trainnc]:
	if not os.path.isfile(rootdir + f):
		logging.error("File doesn't exist: " + rootdir + f)
		print("File doesn't exist: " + rootdir + f)
		exit()


if args.delete:
	for f in [testfeat, valfeat, trainfeat, testfeatnorm, valfeatnorm, trainfeatnorm]:
		if os.path.exists(f):
			sh.rmtree(f)
	
	logging.info("Deleted temporary feature folders")
	exit(0)


def clean_folder(foldername):
	
	if os.path.exists(foldername):
		sh.rmtree(foldername)
		os.makedirs(foldername)
	else:
		os.makedirs(foldername) # should never happen

#network              = autosave_run7_epoch138.autosave
#train                = false
#input_noise_sigma    = 0
#parallel_sequences	 = 2
#ff_output_format	 = htk
#ff_output_kind		 = 838
#feature_period		 = 10
#cuda				 = false
#revert_std			 = true
#ff_input_file 		 = ../../test_reverb_norm.nc
#ff_output_file		 = ./output-test-138/

#print(os.path.basename(args.netname))

if args.cuda:
	tmp_cuda = "true"
	tmp_parallel = "100"
else:
	tmp_cuda = "false"
	tmp_parallel = "3"


command_template = ["currennt", "--network", "./" + netname, "--train","false",
	"--input_noise_sigma", "0", "--parallel_sequences", tmp_parallel, "--ff_output_format", "htk", "--ff_output_kind", "838",
	"--feature_period", "10", "--cuda", tmp_cuda, "--revert_std", "true"]

def generate_features(feat, nc):
	
	try:
		command = command_template[:];
		command.extend(["--ff_input_file", nc, "--ff_output_file", "./" + feat])
		
		logging.info("Command: " + str(command))
		
		tmp_output = sb.check_output(command, stderr=sb.STDOUT, universal_newlines=True)
	
	except sb.CalledProcessError as exc:                                                                                                   
		logging.error("Error generating features " + feat + " . returncode: " + str(exc.returncode) + " output: \n" + str(exc.output))
		print("Error generating features " + feat + " ")
		exit()
		
	else:                                                                                                   
		logging.info("Generated features " + feat + " : \n{}\n".format(tmp_output))   

rename_template = ["rename2mfcc.sh"]

def do_rename(feat):
		
	try:
		command = rename_template[:];
		command.extend([feat])
		
		logging.info("Command: " + str(command))
		
		tmp_output = sb.check_output(command, stderr=sb.STDOUT, universal_newlines=True)
	
	except sb.CalledProcessError as exc:                                                                                                   
		logging.error("Error renaming features " + feat + " . returncode: " + str(exc.returncode) + " output: \n" + str(exc.output))
		print("Error renaming features " + feat + " ")
		exit()
		
	else:                                                                                                   
		logging.info("Renamed features " + feat + " : \n{}\n".format(tmp_output))   

compute_template = ["compute_output_mean_stddev.py"]

def compute_means(feat, saved_means):
		
	try:
		command = compute_template[:];
		command.extend([feat, saved_means])
		
		logging.info("Command: " + str(command))
		
		tmp_output = sb.check_output(command, stderr=sb.STDOUT, universal_newlines=True)
	
	except sb.CalledProcessError as exc:                                                                                                   
		logging.error("Error computing means and stddevs of features " + feat + " . returncode: " + str(exc.returncode) + " output: \n" + str(exc.output))
		print("Error computing means and stddevs of features " + feat + " ")
		exit()
		
	else:                                                                                                   
		logging.info("Computing means and stddevs of features " + feat + " : \n{}\n".format(tmp_output))


normalize_template = ["normalizer.py"]

def do_normalize(feat, saved_means, outfeat):
		
	try:
		command = normalize_template[:];
		command.extend([feat, saved_means, outfeat])
		
		logging.info("Command: " + str(command))
		
		tmp_output = sb.check_output(command, stderr=sb.STDOUT, universal_newlines=True)
	
	except sb.CalledProcessError as exc:                                                                                                   
		logging.error("Error normalizing features " + feat + " . returncode: " + str(exc.returncode) + " output: \n" + str(exc.output))
		print("Error normalizing features " + feat + " ")
		exit()
		
	else:                                                                                                   
		logging.info("Normalized features " + feat + " : \n{}\n".format(tmp_output))  
		
def do_feature_work(feat, outfeat, nc, saved_means):
		
	clean_folder(rootdir + feat)
	
	generate_features(feat, nc)
	
	do_rename(feat)

	compute_means(feat, saved_means)
	
	#sb.call(["htk_mfcc_visualize.py", feat + "0dB/10_bgakzn.mfcc"])
	
	do_normalize(feat, saved_means, outfeat)
	
	#sb.call(["htk_mfcc_visualize.py", outfeat + "0dB/10_bgakzn.mfcc"])
	
if not args.just_test:
	
	logging.info("Started generating features")
	
	if args.inset == "test" or args.inset == "all" :
		
		feat = testfeat
		outfeat = testfeatnorm
		nc = testnc
		saved_means = "./test_means.json"
		
		do_feature_work(feat, outfeat, nc, saved_means)	
	
	if args.inset == "train" or args.inset == "all" :
		
		feat = trainfeat
		outfeat = trainfeatnorm
		nc = trainnc
		saved_means = "./train_means.json"
		
		do_feature_work(feat, outfeat, nc, saved_means)	
		
	if args.inset == "val" or args.inset == "all" :
		
		feat = valfeat
		outfeat = valfeatnorm
		nc = valnc
		saved_means = "./val_means.json"
		
		do_feature_work(feat, outfeat, nc, saved_means)	
		
	logging.info("Finished generating features")
		

# feature score phase


# finish: save results to .ods file or someting
