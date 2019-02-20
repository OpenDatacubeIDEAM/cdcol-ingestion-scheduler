# Datacube Ingestion Scheduler

from configparser import ConfigParser
from entities.LockFile import LockFile
from entities.Connection import Connection
from entities.IngestionTasks import IngestionTasks
from entities.StorageUnit import StorageUnit
from dao.StorageUnit import StorageUnit as DAOStorageUnit
from builtins import Exception
import os, sys, datetime, glob, traceback
from subprocess import CalledProcessError, Popen, PIPE

CONF_FILE = 'settings.conf'

conf = ConfigParser()
conf.read(CONF_FILE)

TO_INGEST = conf.get('paths','to_ingest')
ING_SCRIPT = conf.get('other','ing_script')

WEB_THUMBNAILS = conf.get('paths','web_thumbnails')
THUMB_SCRIPT = conf.get('other', 'thumb_script')
THUMB_X_RES = conf.get('other', 'thumb_x_res')
THUMB_Y_RES = conf.get('other', 'thumb_y_res')
THUMB_COLORS = conf.get('other', 'thumb_colors')

lockfile = LockFile(conf.get('other','lock_file'))
if lockfile.search():
	print ('There\'s an execution in progress')
	sys.exit(1)
else:
	lockfile.write()

try:
	print ('DATACUBE INGESTION SCHEDULER')

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

		print('Running ingestion for ' + stg_unit.name)

		for each_itask in itasks.tasks[stg_unit_id]:

			try:
				each_itask.start_execution_date = str(datetime.datetime.now())
				each_itask.state = each_itask.STATES['EXECUTING_STATE']
				each_itask.save()
				p = Popen([ING_SCRIPT, stg_to_ingest, stg_conf_file, stg_mgen_script], stdout=PIPE, stderr=PIPE)
				stdout, stderr = p.communicate()
				each_itask.end_execution_date = str(datetime.datetime.now())
				each_itask.logs = stdout.decode('ascii')
				each_itask.error_messages = stderr.decode('ascii')
				if stdout.endswith(' 0 failed\n'):
					each_itask.state = each_itask.STATES['COMPLETED_STATE']
					for each_file in glob.glob(stg_to_ingest + '/*.tar.gz' ):
						os.remove(each_file)
				else:
					each_itask.state = each_itask.STATES['FAILED_STATE']
				each_itask.save()
			except CalledProcessError as cpe:
				print('Error running ingestion script: ' + str(cpe))

	for stg_unit_id in itasks.tasks:
		stg_unit = StorageUnit(dao_stgunit.get_by_id(stg_unit_id))
		stg_web_thumbnails = WEB_THUMBNAILS + '/' + stg_unit.name

		print('Generating thumbnails for ' + stg_unit.name)
		try:
			p = Popen([THUMB_SCRIPT, stg_unit.root_dir, stg_web_thumbnails, THUMB_X_RES, THUMB_Y_RES, THUMB_COLORS], stdout=PIPE, stderr=PIPE)
			stdout, stderr = p.communicate()
			with open('thumbnails.log', 'w') as ofile:
				ofile.write(stdout)
			with open('thumbnails.err', 'w') as ofile:
				ofile.write(stderr)
		except CalledProcessError as cpe:
			print('Error generating storage unit thumbnails')

except Exception as e:
	#print 'Error: ' + str(e)
	traceback.print_exc()
finally:
	lockfile.delete()
	dbconn.close()
