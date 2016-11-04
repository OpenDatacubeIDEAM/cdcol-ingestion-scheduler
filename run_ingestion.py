# Datacube Ingestion Scheduler

from ConfigParser import ConfigParser
from dao.Connection import Connection
from dao.IngestTask import IngestTask
from exceptions import Exception
import os, sys

#PID_FILE = TO_INGEST + '/pid.lock'
CONF_FILE = 'settings.conf'

conf = ConfigParser()
conf.read(CONF_FILE)

dbconn = Connection(
			host=conf.get('database','host'),
			port=conf.get('database','port'),
			name=conf.get('database','name'),
			user=conf.get('database','user'),
			password=conf.get('database','password')
			)

dbconn.connect()
itask = IngestTask(dbconn.curr_conn)
print itask.get_completed()

#lockfile = LockFile(PID_FILE)
#if lockfile.search():
#	print 'There\'s an execution in progress'
#	sys.exit(1)
#else:
#	lockfile.write()

#try:
#	print 'DATACUBE INGESTION SHCEDULER'
#	ing_tasks = IngestionTasks()
#	ing_tasks.search_tasks(TO_INGEST)
#except Exception as e:
#	print 'Error: ' + str(e)
#	raise e
#finally:
#	lockfile.delete()
