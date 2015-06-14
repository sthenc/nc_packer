#!/bin/sh

cd "$1"

for dir in `find . -maxdepth 1 -mindepth 1 -type d -printf '%f\n'` ; do
	#echo $dir
	for file in $dir/*.htk; do
		#echo $file
		mv "$file" $dir/"`basename $file .htk`.mfcc"
		#echo "`basename $file .htk`.mfcc"
	done
done


