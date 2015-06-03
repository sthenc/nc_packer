#!/usr/bin/python
import os

komanda_feature = "SMILExtract -C ../MFCC12_E_D_A.conf -logfile smile_train.log -appendLogfile 1 " #-I input.wav -O output.mfcc.htk"


clean_dirpath = "/mnt/data/Fer/diplomski/CHiME2/aasp-chime-grid/train/reverberated/"

clean_prefix = ""

noisy_basepath = "/mnt/data/Fer/diplomski/CHiME2/aasp-chime-grid/train/isolated/"
noisy_dirpaths = [""]

noisy_prefix = ""

input_postfix = ""
output_postfix = ".mfcc.htk"

tmp_dirpath = "./tmp_train/" 

mapfile = "train_map.txt"

os.system('rm -r ' + tmp_dirpath + "*")

os.makedirs(tmp_dirpath + "clean/")
os.makedirs(tmp_dirpath + "noisy/")

for dr in [ "id" + str(i) for i in range(1, 35)]:
	if not os.path.exists(tmp_dirpath + dr):
		os.makedirs(tmp_dirpath + "clean/" + dr)
		os.makedirs(tmp_dirpath + "noisy/" + dr)



def get_filenames_dev(path):
	
	ret = []
	
	svpth = os.getcwd()
	os.chdir(path)
	# stolen from http://www.tutorialspoint.com/python/os_walk.htm
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			ret.append(os.path.join(root, name)[2:])
	
	os.chdir(svpth)
	return ret
	

filenames = get_filenames_dev(clean_dirpath)  # [ 1: 10 ]

print (filenames)
htklist = []

os.chdir(tmp_dirpath)

for f in filenames:
	
	inputfile = clean_dirpath + clean_prefix  + f + input_postfix
	
	outputfile = "clean/" + clean_prefix + f + output_postfix
	
	os.system("touch " + outputfile)
	komanda = komanda_feature + " -I " + inputfile + " -O " + outputfile
	print(komanda)
	os.system(komanda)
	
	
for n in noisy_dirpaths:
	print (n)
	for f in filenames:
		
		inputfile = noisy_basepath + n + noisy_prefix  + f + input_postfix
		
		outputfile = "noisy/" + n + noisy_prefix + f + output_postfix
		
		komanda = komanda_feature  + " -I " + inputfile + " -O " + outputfile
		
		os.system("touch " + outputfile)
		print(komanda)
		os.system(komanda)
		
		htklist.append((n + "/" + f, outputfile, 'clean/' + clean_prefix + f + output_postfix))
	
	

print (htklist)


# write the mapfile for htk2nc
# in format "tag inputpath targetpath"
fajl = open(mapfile, "w")

for h in htklist:
	fajl.write(h[0] + ' 1 ' + h[1] + ' ' + h[2] + "\n")
	
