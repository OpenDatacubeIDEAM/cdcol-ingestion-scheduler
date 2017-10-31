#!/bin/bash

PYTHON='/home/cubo/anaconda2/bin/python'
export GDAL_DATA="${GDAL_DATA:-/usr/share/gdal/1.11}"

echo "$(date) RUNNING INGESTION SCHEDULER"
source /home/cubo/.bashrc
cd /home/cubo/ingestion-scheduler
$PYTHON run_ingestion.py
echo "$(date) DONE"
