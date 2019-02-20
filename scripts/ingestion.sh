#!/bin/bash

# sudo renice -10 $$

# SET VARIABLES
PYTHON='/home/cubo/anaconda/bin/python3'
DATACUBE='/home/cubo/anaconda/bin/datacube3'


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

for archivo in $(find . -maxdepth 1 -name '*.tar.gz' -printf '%f\n')
do

	folder="$basePath/tmp/${archivo%%-*}"
	mkdir -p $folder && tar -xzf $archivo -C $folder

	$PYTHON $mgen_script $folder && $DATACUBE dataset add -a $folder

done

$DATACUBE ingest --executor multiproc $threads -c $configFile
rm -rf "$basePath/tmp"
