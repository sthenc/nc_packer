#!/usr/bin/python
import os

komanda_feature = "SMILExtract -C ../MFCC12_E_D_A.conf -logfile smile.log -noconsoleoutput 1 -appendLogfile 1 " #-I input.wav -O output.mfcc.htk"


clean_dirpath = "/mnt/data/Fer/diplomski/CHiME2/chime2-grid/devel/reverberated/"

clean_prefix = ""

noisy_basepath = "/mnt/data/Fer/diplomski/CHiME2/aasp-chime-grid/devel/isolated/"
noisy_dirpaths = ["0dB", "3dB", "6dB", "9dB", "m3dB", "m6dB"]

noisy_prefix = "/s"

input_prefix = ".wav"
output_prefix = ".mfcc.htk"

tmp_dirpath = "./tmp/" 

mapfile = "dev_map.txt"

os.system('rm -r ' + tmp_dirpath + "*")

for dr in noisy_dirpaths:
	if not os.path.exists(tmp_dirpath + dr):
		os.makedirs(tmp_dirpath + dr)



def get_filenames_dev(path):
	
	ret = os.listdir(path)
	
	return [x.split('.')[0] for x in ret]
	

filenames = get_filenames_dev(clean_dirpath)  [ 1:10 ]

print (filenames)
htklist = []

os.chdir(tmp_dirpath)

for f in filenames:
	
	inputfile = clean_dirpath + clean_prefix  + f + input_prefix
	
	outputfile = clean_prefix + f + output_prefix
	
	komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
	
	os.system(komanda)
	
	
for n in noisy_dirpaths:
	print (n)
	for f in filenames:
		
		inputfile = noisy_basepath + n + noisy_prefix  + f + input_prefix
		
		outputfile = n + noisy_prefix + f + output_prefix
		
		komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
		
		os.system(komanda)
		
		htklist.append((n + "/" + f, outputfile, clean_prefix + f + output_prefix))
	
	

print (htklist)


# write the mapfile for htk2nc
# in format "tag inputpath targetpath"
fajl = open(mapfile, "w")

for h in htklist:
	fajl.write(h[0] + ' 1 ' + h[1] + ' ' + h[2] + "\n")
	
