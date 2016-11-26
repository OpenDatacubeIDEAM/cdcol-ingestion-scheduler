from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

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
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'comments,' +
					'error_messages,' +
					'logs,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'updated_at,' +
					'created_by_id,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask;')
		rows = cur.fetchall()
		return rows

	def get_scheduled(self):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'comments,' +
					'error_messages,' +
					'logs,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'updated_at,' +
					'created_by_id,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['SCHEDULED_STATE'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_executing(self):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'comments,' +
					'error_messages,' +
					'logs,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'updated_at,' +
					'created_by_id,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['EXECUTING_STATE'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_failed(self):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'comments,' +
					'error_messages,' +
					'logs,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'updated_at,' +
					'created_by_id,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['FAILED_STATED'] + '\';')
		rows = cur.fetchall()
		return rows

	def get_completed(self):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id,' +
					'state,' +
					'comments,' +
					'error_messages,' +
					'logs,' +
					'start_execution_date,' +
					'end_execution_date,' +
					'created_at,' +
					'updated_at,' +
					'created_by_id,' +
					'storage_unit_id ' +
					'FROM ingest_ingesttask ' +
					'WHERE state = \'' + self.STATES['COMPLETED_STATE'] + '\';')
		rows = cur.fetchall()
		return rows
