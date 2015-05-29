#!/usr/bin/python

import os

os.chdir('./tmp_test/')

komanda = 'htk2nc test_map.txt ../test.nc'

os.system(komanda)

import time
import datetime

ts = time.time()

stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

os.system('cp ../test.nc ../backup/test' + stamp + '.nc')

