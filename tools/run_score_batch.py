#!/usr/bin/python
import os

run_root="/mnt/data/Fer/diplomski/training_currennt/speech_autoencoding_chime/mreze-2015-05-28/"



index = 204 # 178 # 142 # 73

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
#nets="""run7/autosave_run7_epoch171.autosave
#run7/autosave_run7_epoch167.autosave
#run7/autosave_run7_epoch163.autosave
#run7/autosave_run7_epoch159.autosave
#run7/autosave_run7_epoch155.autosave
#run7/autosave_run7_epoch151.autosave
#run7/autosave_run7_epoch147.autosave
#run7/autosave_run7_epoch145.autosave
#run7/autosave_run7_epoch143.autosave
#run7/autosave_run7_epoch139.autosave
#run7/autosave_run7_epoch138.autosave
#run7/autosave_run7_epoch137.autosave
#run7/autosave_run7_epoch135.autosave
#run7/autosave_run7_epoch131.autosave
#run7/autosave_run7_epoch127.autosave
#run7/autosave_run7_epoch123.autosave
#run7/autosave_run7_epoch119.autosave
#run7/autosave_run7_epoch119.autosave
#run7/autosave_run7_epoch115.autosave
#run7/autosave_run7_epoch111.autosave
#run7/autosave_run7_epoch107.autosave
#run7/autosave_run7_epoch103.autosave
#nets="""run7/autosave_run7_epoch099.autosave
#run6/autosave_run6_epoch096.autosave
#run6/autosave_run6_epoch092.autosave
#run6/autosave_run6_epoch088.autosave
#run6/autosave_run6_epoch086.autosave
#run6/autosave_run6_epoch083.autosave
#run6/autosave_run6_epoch080.autosave
#run6/autosave_run6_epoch076.autosave
#run6/autosave_run6_epoch073.autosave
#run6/autosave_run6_epoch070.autosave
#run6/autosave_run6_epoch068.autosave
#run6/autosave_run6_epoch064.autosave
#run6/autosave_run6_epoch061.autosave
#run6/autosave_run6_epoch057.autosave
#run6/autosave_run6_epoch054.autosave
#run6/autosave_run6_epoch053.autosave
#run6/autosave_run6_epoch048.autosave
#run6/autosave_run6_epoch047.autosave
#run6/autosave_run6_epoch045.autosave
#run6/autosave_run6_epoch042.autosave
#run6/autosave_run6_epoch039.autosave
#run6/autosave_run6_epoch038.autosave
#run6/autosave_run6_epoch036.autosave
#run6/autosave_run6_epoch033.autosave
#run6/autosave_run6_epoch032.autosave
#run6/autosave_run6_epoch031.autosave
#run6/autosave_run6_epoch029.autosave
#run6/autosave_run6_epoch028.autosave
#nets="""run6/autosave_run6_epoch023.autosave
#run6/autosave_run6_epoch022.autosave
#run6/autosave_run6_epoch021.autosave
#run6/autosave_run6_epoch019.autosave
#run6/autosave_run6_epoch017.autosave
#run6/autosave_run6_epoch015.autosave
#run6/autosave_run6_epoch014.autosave
#run6/autosave_run6_epoch013.autosave
#run6/autosave_run6_epoch011.autosave
#run6/autosave_run6_epoch010.autosave
#run6/autosave_run6_epoch008.autosave
#run6/autosave_run6_epoch007.autosave
#run6/autosave_run6_epoch006.autosave
#run6/autosave_run6_epoch005.autosave
#run6/autosave_run6_epoch004.autosave
#run6/autosave_run6_epoch003.autosave
#run6/autosave_run6_epoch002.autosave
#run6/autosave_run6_epoch001.autosave
#run8/autosave_run8_epoch232.autosave
#run8/autosave_run8_epoch231.autosave
#run8/autosave_run8_epoch230.autosave
#run8/autosave_run8_epoch229.autosave
#run8/autosave_run8_epoch228.autosave
#run8/autosave_run8_epoch227.autosave
#run8/autosave_run8_epoch226.autosave
#run8/autosave_run8_epoch225.autosave
#run8/autosave_run8_epoch224.autosave
#run8/autosave_run8_epoch223.autosave
#run8/autosave_run8_epoch222.autosave
#run8/autosave_run8_epoch221.autosave
#run8/autosave_run8_epoch220.autosave
#run8/autosave_run8_epoch219.autosave
#run8/autosave_run8_epoch218.autosave
#run8/autosave_run8_epoch217.autosave
#run8/autosave_run8_epoch216.autosave
#run8/autosave_run8_epoch215.autosave
#run8/autosave_run8_epoch214.autosave
#run8/autosave_run8_epoch213.autosave
#run8/autosave_run8_epoch212.autosave
#run8/autosave_run8_epoch211.autosave
#run8/autosave_run8_epoch210.autosave
#run8/autosave_run8_epoch209.autosave
#run8/autosave_run8_epoch208.autosave
#run8/autosave_run8_epoch207.autosave
#run8/autosave_run8_epoch206.autosave
#run8/autosave_run8_epoch205.autosave
#run8/autosave_run8_epoch204.autosave
#run8/autosave_run8_epoch203.autosave
#run8/autosave_run8_epoch202.autosave
#run8/autosave_run8_epoch201.autosave
#run8/autosave_run8_epoch200.autosave
#run8/autosave_run8_epoch199.autosave
#run8/autosave_run8_epoch198.autosave
#run8/autosave_run8_epoch197.autosave
#run8/autosave_run8_epoch196.autosave
#run8/autosave_run8_epoch195.autosave
#run8/autosave_run8_epoch194.autosave
#run8/autosave_run8_epoch193.autosave
#run8/autosave_run8_epoch192.autosave
#run8/autosave_run8_epoch191.autosave
#run8/autosave_run8_epoch190.autosave
#run8/autosave_run8_epoch189.autosave
#run8/autosave_run8_epoch188.autosave
#run8/autosave_run8_epoch187.autosave
#run8/autosave_run8_epoch186.autosave
#run8/autosave_run8_epoch185.autosave
#run8/autosave_run8_epoch184.autosave
#run8/autosave_run8_epoch183.autosave
#run8/autosave_run8_epoch182.autosave
#nets="""run8/autosave_run8_epoch233.autosave
#run8/autosave_run8_epoch234.autosave
#run9/autosave_run9_epoch234.autosave
#run9/autosave_run9_epoch233.autosave
#run9/autosave_run9_epoch232.autosave
#run9/autosave_run9_epoch231.autosave
#run9/autosave_run9_epoch230.autosave
#run9/autosave_run9_epoch229.autosave
#run9/autosave_run9_epoch228.autosave
#run9/autosave_run9_epoch227.autosave
#run9/autosave_run9_epoch226.autosave
#run9/autosave_run9_epoch225.autosave
#run9/autosave_run9_epoch224.autosave
#run9/autosave_run9_epoch223.autosave
#run9/autosave_run9_epoch222.autosave
#run9/autosave_run9_epoch221.autosave
#run9/autosave_run9_epoch220.autosave
#run9/autosave_run9_epoch219.autosave
#run9/autosave_run9_epoch218.autosave
#run9/autosave_run9_epoch217.autosave
#run9/autosave_run9_epoch216.autosave
#run9/autosave_run9_epoch215.autosave
#run9/autosave_run9_epoch214.autosave
#run9/autosave_run9_epoch213.autosave
#run9/autosave_run9_epoch212.autosave
#run9/autosave_run9_epoch211.autosave
#run9/autosave_run9_epoch210.autosave
#run9/autosave_run9_epoch209.autosave
#run9/autosave_run9_epoch208.autosave
#run9/autosave_run9_epoch207.autosave
#run9/autosave_run9_epoch206.autosave
#run9/autosave_run9_epoch205.autosave
#run9/autosave_run9_epoch204.autosave
#run9/autosave_run9_epoch203.autosave
#run9/autosave_run9_epoch202.autosave
#run9/autosave_run9_epoch201.autosave
#nets="""run10/autosave_run10_epoch181.autosave
#run10/autosave_run10_epoch182.autosave
#run10/autosave_run10_epoch183.autosave
#run10/autosave_run10_epoch184.autosave
#run10/autosave_run10_epoch185.autosave
#run10/autosave_run10_epoch186.autosave
#run10/autosave_run10_epoch187.autosave
#run10/autosave_run10_epoch188.autosave
#run10/autosave_run10_epoch189.autosave
#run10/autosave_run10_epoch190.autosave
#run10/autosave_run10_epoch191.autosave
#run10/autosave_run10_epoch192.autosave
#run10/autosave_run10_epoch193.autosave
#run10/autosave_run10_epoch194.autosave
#run10/autosave_run10_epoch195.autosave
#run10/autosave_run10_epoch196.autosave
#run10/autosave_run10_epoch197.autosave
#run10/autosave_run10_epoch198.autosave
#run10/autosave_run10_epoch199.autosave
#run10/autosave_run10_epoch200.autosave
#run10/autosave_run10_epoch201.autosave
#run10/autosave_run10_epoch202.autosave
#run10/autosave_run10_epoch203.autosave
#run10/autosave_run10_epoch204.autosave
#run10/autosave_run10_epoch205.autosave
#run10/autosave_run10_epoch206.autosave
nets="""run10/autosave_run10_epoch207.autosave
run10/autosave_run10_epoch208.autosave
run10/autosave_run10_epoch209.autosave
run10/autosave_run10_epoch210.autosave
run10/autosave_run10_epoch211.autosave
run10/autosave_run10_epoch212.autosave
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
