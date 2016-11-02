# Datacube Ingestion Scheduler

from utils.LockFile import LockFile
from utils.IngestionTasks import IngestionTasks
from exceptions import Exception
import os, sys

TO_INGEST = os.environ['TO_INGEST']
PID_FILE = TO_INGEST + '/pid.lock'

lockfile = LockFile(PID_FILE)
if lockfile.search():
	print 'There\'s an execution in progress'
	sys.exit(1)
else:
	lockfile.write()

try:
	print 'DATACUBE INGESTION SHCEDULER'
	ing_tasks = IngestionTasks()
	ing_tasks.search_tasks(TO_INGEST)
except Exception as e:
	print 'Error: ' + str(e)
	raise e
finally:
	lockfile.delete()
