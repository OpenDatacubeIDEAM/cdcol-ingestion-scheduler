from psycopg2.extensions import connection

class IngestTask():

	STATES= {
			'SCHEDULED_STATE':'1',
			'EXECUTING_STATE':'2',
			'FAILED_STATED':'3',
			'COMPLETED_STATE':'4'
			}

	def __init__(self, connection):
		self.conn = connection

	def get_all(self):
		cur = self.conn.cursor()
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'errors,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask;')
		rows = cur.fetchall()
		return rows

	def get_scheduled(self):
		cur = self.conn.cursor()
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'errors,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['SCHEDULED_STATE'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_executing(self):
		cur = self.conn.cursor()
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'errors,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['EXECUTING_STATE'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_failed(self):
		cur = self.conn.cursor()
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'errors,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['FAILED_STATED'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_completed(self):
		cur = self.conn.cursor()
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'errors,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['COMPLETED_STATE'] + '\';')
		rows = cur.fetchall()
		return rows
