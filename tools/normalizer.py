#!/usr/bin/python

import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

import htkmfc as hm

import argparse
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument("foldername", help="foldername for tree with .mfcc features")
parser.add_argument("loadname", help="file to load means and stddevs from")
parser.add_argument("normfolder", help="where to save  normalized features")
args = parser.parse_args()



htk_means = np.array([  1.15722319e-08,  -2.13178994e-09,  -4.05115476e-10,
        -6.43738949e-09,   1.82928064e-10,   3.69764212e-09,
        -1.54024725e-09,   1.86700352e-09,  -3.08947228e-10,
         2.29094022e-09,  -1.66058373e-09,   8.95853859e-10,
         1.87480430e+01,   1.83920172e-03,   4.87789175e-03,
        -3.37601211e-04,  -6.89982474e-04,  -8.84367010e-04,
        -1.61661255e-03,   3.20384575e-03,   1.12076531e-03,
        -2.42963737e-03,  -3.20266388e-03,  -7.05282956e-03,
        -7.02085172e-03,   7.38239701e-04,  -7.93265583e-06,
        -4.59731051e-04,  -3.25283569e-04,   8.35059739e-05,
         3.50690285e-06,   1.36857779e-04,  -5.92782648e-04,
        -5.67035838e-04,   1.59946519e-04,   4.16375112e-05,
         5.96704910e-04,   2.46795305e-04,   1.91299258e-04])

htk_stds = np.array([ 5.01052426,  6.0709671 ,  6.3988848 ,  6.4326679 ,  7.05289745,
        6.52335284,  6.66776467,  6.64381026,  6.44838521,  6.17903677,
        6.20714265,  5.59613917,  1.31109425,  0.97349199,  1.14672472,
        1.25496237,  1.41486924,  1.54320173,  1.51970999,  1.59762707,
        1.62821243,  1.60996583,  1.57246291,  1.57479229,  1.44945802,
        0.23108161,  0.354538  ,  0.41511243,  0.47434781,  0.55798064,
        0.61024786,  0.62611209,  0.66455343,  0.68386709,  0.67936381,
        0.66838117,  0.66832734,  0.62084678,  0.09018718])


import json

infajl = open(args.loadname, "r")
tmp = json.load(infajl)
infajl.close()

ops_means = np.array(tmp[0])
ops_stds = np.array(tmp[1])

print (ops_means)
print (ops_stds)

new_means = ops_means - htk_means
new_stds  = ops_stds / htk_stds

#x = np.linspace(1, len(htk_means), len(htk_means))

#plt.plot(x, htk_means, label = 'htk_means')
#plt.plot(x, ops_means, label = 'ops_means')
#plt.plot(x, new_means, label = 'new_means')

#plt.legend(loc = 'upper right')
#plt.show()

#plt.plot(x, htk_stds, label = 'htk_stds')
#plt.plot(x, ops_stds, label = 'ops_stds')
#plt.plot(x, new_stds, label = 'new_stds')

#plt.legend(loc = 'upper right')
#plt.show()

input_folder = args.foldername
output_folder = args.normfolder

import os


extension = 'mfcc'
print (input_folder)

dirs = [ x for x in os.listdir(input_folder) if os.path.isdir(input_folder + x) ]
print(dirs)

filenames = []

for d in dirs:
	filenames.extend( [d + "/" + f for f in os.listdir(input_folder + d) if f.split('.')[1] == extension ] ) 

print(filenames)




