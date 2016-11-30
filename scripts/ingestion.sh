#!/bin/bash

# sudo renice -10 $$

# SET VARIABLES
#nimg=0
basePath="$1" # Storage Unit folder to Ingest
configFile="$2" # Ingestion file on YAML format
mgen_script="$3" # Metadata generation script on python
threads=$( expr $(grep -c ^processor /proc/cpuinfo) - 1) # Threads =  Number of cores - 1

# CHANGE TO PATH TO INGEST
cd $basePath

# If the processor has only 1 core
if [ $threads -eq 0 ] 
then
	threads=1
fi

for archivo in *.tar.gz
do

	folder="$basePath/tmp/${archivo%%-*}"
	mkdir -p $folder && tar -xzf $archivo -C $folder

	python $mgen_script $folder && datacube dataset add -a $folder

	#((nimg++))
	#if(( $nimg % 18 == 0 ))
	#then 
		#datacube ingest --executor multiproc $threads -c $configFile
	#	rm -rf "$folder"
	#fi
done

echo "datacube ingest --executor multiproc $threads -c $configFile"
rm -rf "$basePath/tmp"
