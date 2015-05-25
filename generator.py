#!/usr/bin/python

komanda_feature = "SMILExtract -C ./MFCC12_E_D_A.conf " #-I input.wav -O output.mfcc.htk"


clean_dirpath = "./"

clean_prefix = "clean_"

noisy_prefix = "9dB_s"

input_prefix = ".wav"
output_prefix = ".mfcc.htk"

filenames = [ "1_bgaa9a" ]  

noisy_basepath = "."
noisy_dirpaths = ["/"]

tmp_dirpath = "./tmp" 


htklist = []

import os

for f in filenames:
	
	inputfile = clean_dirpath + clean_prefix  + f + input_prefix
	
	outputfile = tmp_dirpath + clean_prefix + f + output_prefix
	
	komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
	
	os.system(komanda)
	
	#htklist.append(outputfile)
	
	
for n in noisy_dirpaths:
	for f in filenames:
		
		inputfile = noisy_basepath + n + noisy_prefix  + f + input_prefix
		
		outputfile = tmp_dirpath + n + noisy_prefix + f + output_prefix
		
		komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
		
		os.system(komanda)
		
		htklist.append((outputfile, tmp_dirpath + clean_prefix + f + output_prefix))
	
	

print (htklist)
