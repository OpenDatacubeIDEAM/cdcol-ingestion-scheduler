#!/bin/bash

PYTHON='/home/cubo/anaconda/bin/python3'
export GDAL_DATA="${GDAL_DATA:-/usr/share/gdal/1.11}"

echo "$(date) RUNNING INGESTION SCHEDULER"
source /home/cubo/.bashrc
cd /home/cubo/ingestion-scheduler
$PYTHON run_ingestion.py
echo "$(date) DONE"
