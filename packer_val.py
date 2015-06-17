#!/usr/bin/python

import os

os.chdir('./tmp_val/')

komanda = 'htk2nc val_map.txt ../dev.nc'


os.system(komanda)

import time
import datetime

ts = time.time()

stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

os.system('cp ../dev.nc ../backup/dev' + stamp + '.nc')

