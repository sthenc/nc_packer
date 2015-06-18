#!/usr/bin/python
import os

run_root="/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/mreze-2015-05-28/"



index = 23

#nets ="""
#run8/autosave_run8_epoch216.autosave
#run8/autosave_run8_epoch212.autosave
#run8/autosave_run8_epoch208.autosave
#run8/autosave_run8_epoch204.autosave
#run8/autosave_run8_epoch200.autosave
#run8/autosave_run8_epoch196.autosave
#run8/autosave_run8_epoch192.autosave
#run8/autosave_run8_epoch188.autosave
#run8/autosave_run8_epoch184.autosave
#run8/autosave_run8_epoch182.autosave
#run7/autosave_run7_epoch211.autosave
#run7/autosave_run7_epoch207.autosave
#run7/autosave_run7_epoch203.autosave
#run7/autosave_run7_epoch199.autosave
#run7/autosave_run7_epoch195.autosave
#run7/autosave_run7_epoch191.autosave
#run7/autosave_run7_epoch187.autosave
#run7/autosave_run7_epoch183.autosave
#run7/autosave_run7_epoch181.autosave
#run7/autosave_run7_epoch180.autosave
#run7/autosave_run7_epoch179.autosave
#run7/autosave_run7_epoch175.autosave
nets="""run7/autosave_run7_epoch171.autosave
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
run7/autosave_run7_epoch99.autosave
run6/autosave_run6_epoch96.autosave
run6/autosave_run6_epoch92.autosave
run6/autosave_run6_epoch88.autosave
run6/autosave_run6_epoch86.autosave
run6/autosave_run6_epoch83.autosave
run6/autosave_run6_epoch80.autosave
run6/autosave_run6_epoch76.autosave
run6/autosave_run6_epoch73.autosave
run6/autosave_run6_epoch70.autosave
run6/autosave_run6_epoch68.autosave
run6/autosave_run6_epoch64.autosave
run6/autosave_run6_epoch61.autosave
run6/autosave_run6_epoch57.autosave
run6/autosave_run6_epoch54.autosave
run6/autosave_run6_epoch53.autosave
run6/autosave_run6_epoch48.autosave
run6/autosave_run6_epoch47.autosave
run6/autosave_run6_epoch45.autosave
run6/autosave_run6_epoch42.autosave
run6/autosave_run6_epoch39.autosave
run6/autosave_run6_epoch38.autosave
run6/autosave_run6_epoch36.autosave
run6/autosave_run6_epoch33.autosave
run6/autosave_run6_epoch32.autosave
run6/autosave_run6_epoch31.autosave
run6/autosave_run6_epoch29.autosave
run6/autosave_run6_epoch28.autosave
run6/autosave_run6_epoch23.autosave
run6/autosave_run6_epoch22.autosave
run6/autosave_run6_epoch21.autosave
run6/autosave_run6_epoch19.autosave
run6/autosave_run6_epoch17.autosave
run6/autosave_run6_epoch15.autosave
run6/autosave_run6_epoch14.autosave
run6/autosave_run6_epoch13.autosave
run6/autosave_run6_epoch11.autosave
run6/autosave_run6_epoch10.autosave
run6/autosave_run6_epoch8.autosave
run6/autosave_run6_epoch7.autosave
run6/autosave_run6_epoch6.autosave
run6/autosave_run6_epoch5.autosave
run6/autosave_run6_epoch4.autosave
run6/autosave_run6_epoch3.autosave
run6/autosave_run6_epoch2.autosave
run6/autosave_run6_epoch1.autosave
"""

nets = [n.strip() for n in nets.split("\n") if len(n.strip()) > 0]

#print(nets)

command_template = "chime_scorer.py val all "

# idemo od test_0000
#test_0001 run_root/

for i in range(0, len(nets)):
	command = command_template + "test_%04d " % (i + index) + run_root + nets[i]
	
	os.system(command)
