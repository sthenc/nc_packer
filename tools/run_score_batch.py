#!/usr/bin/python
import os

run_root="/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/mreze-2015-05-28/"



index = 1001 # 178 # 142 # 73

nets ="""
run7/autosave_run7_epoch211.autosave
run7/autosave_run7_epoch207.autosave
run7/autosave_run7_epoch203.autosave
run7/autosave_run7_epoch199.autosave
run7/autosave_run7_epoch195.autosave
run7/autosave_run7_epoch191.autosave
run7/autosave_run7_epoch187.autosave
run7/autosave_run7_epoch183.autosave
run7/autosave_run7_epoch181.autosave
run7/autosave_run7_epoch180.autosave
run7/autosave_run7_epoch179.autosave
run7/autosave_run7_epoch175.autosave
run7/autosave_run7_epoch171.autosave
run7/autosave_run7_epoch167.autosave
run7/autosave_run7_epoch163.autosave
run7/autosave_run7_epoch159.autosave
run7/autosave_run7_epoch155.autosave
run7/autosave_run7_epoch151.autosave
run7/autosave_run7_epoch147.autosave
run7/autosave_run7_epoch145.autosave
run7/autosave_run7_epoch143.autosave
run7/autosave_run7_epoch139.autosave
run7/autosave_run7_epoch138.autosave
run7/autosave_run7_epoch137.autosave
run7/autosave_run7_epoch135.autosave
run7/autosave_run7_epoch131.autosave
run7/autosave_run7_epoch127.autosave
run7/autosave_run7_epoch123.autosave
run7/autosave_run7_epoch119.autosave
run7/autosave_run7_epoch119.autosave
run7/autosave_run7_epoch115.autosave
run7/autosave_run7_epoch111.autosave
run7/autosave_run7_epoch107.autosave
run7/autosave_run7_epoch103.autosave
run7/autosave_run7_epoch099.autosave
run6/autosave_run6_epoch096.autosave
run6/autosave_run6_epoch092.autosave
run6/autosave_run6_epoch088.autosave
run6/autosave_run6_epoch086.autosave
run6/autosave_run6_epoch083.autosave
run6/autosave_run6_epoch080.autosave
run6/autosave_run6_epoch076.autosave
run6/autosave_run6_epoch073.autosave
run6/autosave_run6_epoch070.autosave
run6/autosave_run6_epoch068.autosave
run6/autosave_run6_epoch064.autosave
run6/autosave_run6_epoch061.autosave
run6/autosave_run6_epoch057.autosave
run6/autosave_run6_epoch054.autosave
run6/autosave_run6_epoch053.autosave
run6/autosave_run6_epoch048.autosave
run6/autosave_run6_epoch047.autosave
run6/autosave_run6_epoch045.autosave
run6/autosave_run6_epoch042.autosave
run6/autosave_run6_epoch039.autosave
run6/autosave_run6_epoch038.autosave
run6/autosave_run6_epoch036.autosave
run6/autosave_run6_epoch033.autosave
run6/autosave_run6_epoch032.autosave
run6/autosave_run6_epoch031.autosave
run6/autosave_run6_epoch029.autosave
run6/autosave_run6_epoch028.autosave
run6/autosave_run6_epoch023.autosave
run6/autosave_run6_epoch022.autosave
run6/autosave_run6_epoch021.autosave
run6/autosave_run6_epoch019.autosave
run6/autosave_run6_epoch017.autosave
run6/autosave_run6_epoch015.autosave
run6/autosave_run6_epoch014.autosave
run6/autosave_run6_epoch013.autosave
run6/autosave_run6_epoch011.autosave
run6/autosave_run6_epoch010.autosave
run6/autosave_run6_epoch008.autosave
run6/autosave_run6_epoch007.autosave
run6/autosave_run6_epoch006.autosave
run6/autosave_run6_epoch005.autosave
run6/autosave_run6_epoch004.autosave
run6/autosave_run6_epoch003.autosave
run6/autosave_run6_epoch002.autosave
run6/autosave_run6_epoch001.autosave
"""

nets = [n.strip() for n in nets.split("\n") if len(n.strip()) > 0]

#print(nets)

command_template = "chime_scorer.py val all "

# idemo od test_0000
#test_0001 run_root/

for i in range(0, len(nets)):
	command = command_template + "test_%04d " % (i + index) + run_root + nets[i]
	
	os.system(command)
	
	command = command_template + "--delete test_%04d " % (i + index) + run_root + nets[i]
	
	os.system(command)
