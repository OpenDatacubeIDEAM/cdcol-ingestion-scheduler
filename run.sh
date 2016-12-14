#!/bin/bash

PYTHON='anaconda_python_bin'

echo "$(date) RUNNING INGESTION SCHEDULER"
source /home/cubo/.bashrc
cd /home/cubo/ingestion
$PYTHON run_ingestion.py
echo "$(date) DONE"
