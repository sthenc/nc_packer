#!/bin/bash

cd "$1"

for dir in `find . -maxdepth 1 -mindepth 1 -type d -printf '%f\n'` ; do
	#echo $dir
	for file in $dir/*.*; do
		#echo $file
		file_basename=`basename $file`
		echo $file_basename
		file_basename=${file_basename%%.*}
		
		echo $file_basename
		mv "$file" $dir/$file_basename".mfcc"
		
		#echo "`basename $file .htk`.mfcc"
	done
done


