from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

class IngestTask():

	def __init__(self, connection):
		self.conn = connection

	def get_by_state(self, state):
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
					'WHERE state = \'' + state + '\';')
		rows = cur.fetchall()
		return rows

	def update(_id, state, comments, error_messages, logs, start_execution_date, end_execution_date, created_at, updated_at, created_by_id, storage_unit_id):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('UPDATE ingest_ingesttask SET ' +
					'state=' + state + ',' +
					'comments="' + comments + '",' +
					'error_messages="' + error_messages + '",' +
					'logs="' + logs + '",' +
					'start_execution_date=' + start_execution_date + ',' +
					'end_execution_date=' + end_execution_date + ',' +
					'created_at=' + created_at + ',' +
					'updated_at=' + updated_at + ',' +
					'created_by_id=' + created_by_id + ',' +
					'storage_unit_id=' + storage_unit_id + ' ' +
					'FROM ingest_ingesttask ' +
					'WHERE id=' + _id + ';')
		self.conn.commit()
		cur.close()
