#!/usr/bin/python

import ezodf as od
import numpy as np
import time
import datetime
import os


results_root = "/mnt/data/Fer/diplomski/training_currennt/results/"

def save_score(strid, results):
	
	print("save_score called")
	
	# initialize empty table
	
	results_file = results_root + "results.ods"
	
	if os.path.isfile(results_file):
		spreadsheet = od.opendoc(filename = results_file)
	else:
		spreadsheet = od.newdoc(doctype="ods", filename = results_file)
	
	sheets = spreadsheet.sheets
	
	ts = time.time()

	stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S') + "_" + str(ts)
	
	sheetid = strid + "#" + stamp
	
	sheets.append(od.Table(sheetid))
	
	sheet = sheets[sheetid]
	
	sheet[0,0].set_value("strid")
	sheet[0,1].set_value("dataset")
	sheet[0,2].set_value("classifier")
	sheet[0,3].set_value("-6dB")
	sheet[0,4].set_value("-3dB")
	sheet[0,5].set_value(" 0dB")
	sheet[0,6].set_value(" 3dB")
	sheet[0,7].set_value(" 6dB")
	sheet[0,8].set_value(" 9dB")
	sheet[0,9].set_value("mean")

	index = 1

	for r in results:

		row = results[r]
		
		sheet[index, 1].set_value(r[0]) # dataset name
		sheet[index, 2].set_value(r[1]) # classifier name

		for i in range(0, len(row)):
			sheet[index, 3 + i].set_value(row[i] / 100.0, "percentage")

		sheet[index,9].formula = "=AVERAGE(D" + str(index+1)  + ":I" + str(index+1) + ")"
		
		index += 1

	spreadsheet.save()
	
if __name__ == "__main__":
	
	save_score("proba", { ("nijedan",  "random"): [1, 2, 3, 4, 5, 6.7], ("nijedan2",  "random2"): [10, 2, 3, 4, 5, 6.7] } )
