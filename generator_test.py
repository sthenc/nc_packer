#!/usr/bin/python
import os

komanda_feature = "SMILExtract -C ../MFCC12_E_D_A.conf -logfile smile_test.log -appendLogfile 1 " #-I input.wav -O output.mfcc.htk"


noisy_basepath = "/mnt/data/Fer/diplomski/CHiME2/aasp-chime-grid/test/isolated/"
noisy_dirpaths = ["0dB", "3dB", "6dB", "9dB", "m3dB", "m6dB"]

noisy_prefix = ""

input_prefix = ".wav"
output_prefix = ".mfcc.htk"

tmp_dirpath = "./tmp_test/" 

mapfile = "test_map.txt"

os.system('rm -r ' + tmp_dirpath + "*")

for dr in noisy_dirpaths:
	if not os.path.exists(tmp_dirpath + dr):
		os.makedirs(tmp_dirpath + dr)



def get_filenames_dev(path):
	
	ret = []
	
	svpth = os.getcwd()
	os.chdir(path)
	# stolen from http://www.tutorialspoint.com/python/os_walk.htm
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			ret.append(os.path.join(root, name)[2:])
		for name in dirs:
			ret.append(os.path.join(root, name)[2:])
	
	
	os.chdir(svpth)
	return  [x.split('.')[0] for x in ret]
	

filenames = get_filenames_dev(noisy_basepath) # [0:10]

print (filenames)
htklist = []

os.chdir(tmp_dirpath)
	
for f in filenames:
	
	inputfile = noisy_basepath + noisy_prefix  + f + input_prefix
	
	outputfile = noisy_prefix + f + output_prefix
	
	komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
	
	os.system(komanda)
	
	htklist.append((f, outputfile))

	

print (htklist)


# write the mapfile for htk2nc
# in format "tag inputpath targetpath"
fajl = open(mapfile, "w")

for h in htklist:
	fajl.write(h[0] + ' 1 ' + h[1] +  "\n")
	
