#!/bin/sh

for dir in 0dB  3dB  6dB  9dB  m3dB  m6dB ; do
	#echo $dir
	for file in $dir/*.htk; do
		#echo $file
		mv "$file" $dir/"`basename $file .htk`.mfcc"
		#echo "`basename $file .htk`.mfcc"
	done
done


