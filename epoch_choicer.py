#!/usr/bin/python

# opposite direction because recent data is more important

suf  = ".autosave"

pref1 = "run8/autosave_run8_epoch"

ch1 = [i for i in range(216, 184, -4)]

ch1.extend([ 184, 182])

for c in ch1:
	print(pref1 + ("%03d" % c) + suf)


pref2 = "run7/autosave_run7_epoch"

ch2 = [181, 180, 171, 145, 138, 137, 119]

ch2.extend([i for i in range(211, 97, -4)])

ch2.sort(reverse=True)

for c in ch2:
	print(pref2 + ("%03d" % c) + suf)


pref3 = "run6/autosave_run6_epoch"


ch3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 28, 29]

ch3.extend([31, 32, 33, 36, 38, 39, 42, 45, 47, 48, 53, 54, 57, 61, 64, 68, 70])
ch3.extend([73, 76, 80, 83, 86, 88, 92, 96])

ch3.sort(reverse=True)

for c in ch3:
	print(pref3 + ("%03d" % c) + suf)


pref4 = "run8/autosave_run8_epoch"

ch4 = [i for i in range(234, 181, -1)]

for c in ch4:
	print(pref4 + ("%03d" % c) + suf)


pref5 = "run9/autosave_run9_epoch"

ch5 = [i for i in range(234, 200, -1)]

for c in ch5:
	print(pref5 + ("%03d" % c) + suf)
	
