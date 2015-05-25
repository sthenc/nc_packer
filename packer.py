#!/usr/bin/python

import os

os.chdir('./tmp/')

komanda = 'htk2nc dev_map.txt ../dev.nc'

os.system(komanda)
