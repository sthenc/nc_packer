#!/usr/bin/python

import os

os.chdir('./tmp_train/')

komanda = 'htk2nc train_map.txt ../train.nc'

os.system(komanda)

import time
import datetime

ts = time.time()

stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

os.system('cp ../train.nc ../backup/train_' + stamp + '.nc')

