#!/usr/bin/python

import os

os.chdir('./tmp_train/')

komanda = 'htk2nc train_map.txt ../train.nc'

os.system(komanda)
