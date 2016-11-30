# Datacube Ingestion Scheduler

from ConfigParser import ConfigParser
from entities.LockFile import LockFile
from entities.Connection import Connection
from entities.IngestionTasks import IngestionTasks
from entities.StorageUnit import StorageUnit
from dao.StorageUnit import StorageUnit as DAOStorageUnit
from exceptions import Exception
import os, sys, subprocess
from subprocess import CalledProcessError

CONF_FILE = 'settings.conf'

conf = ConfigParser()
conf.read(CONF_FILE)

TO_INGEST = conf.get('paths','to_ingest')
ING_SCRIPT = conf.get('other','ing_script')

lockfile = LockFile(conf.get('other','lock_file'))
if lockfile.search():
	print 'There\'s an execution in progress'
	sys.exit(1)
else:
	lockfile.write()

try:
	print 'DATACUBE INGESTION SHCEDULER'

	dbconn = Connection(
				host=conf.get('database','host'),
				port=conf.get('database','port'),
				name=conf.get('database','name'),
				user=conf.get('database','user'),
				password=conf.get('database','password')
				)

	dbconn.connect()
	itasks = IngestionTasks(dbconn.curr_conn)
	itasks.load_scheduled()
	dao_stgunit = DAOStorageUnit(dbconn.curr_conn)
	for stg_unit_id in itasks.tasks:
		stg_unit = StorageUnit(dao_stgunit.get_by_id(stg_unit_id))

		stg_to_ingest =  TO_INGEST + '/' + stg_unit.name
		stg_conf_file = stg_unit.root_dir + '/' + stg_unit.ingest_file
		stg_mgen_script = stg_unit.root_dir + '/' + stg_unit.metadata_generation_script
		
		try:
			subprocess.check_output([ING_SCRIPT, stg_to_ingest, stg_conf_file, stg_mgen_script])
		except CalledProcessError as cpe:
			print 'Error running ingestion script: ' + str(cpe)

except Exception as e:
	print 'Error: ' + str(e)
	raise e
finally:
	lockfile.delete()
