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

	def update(self, _id, state, comments, error_messages, logs, start_execution_date, end_execution_date, created_at, updated_at, created_by_id, storage_unit_id):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		query = ('UPDATE ingest_ingesttask SET ' +
				'state=' + str(state) + ', ' +
				'comments=\'' + str(comments) + '\',' +
				'error_messages=\'' + str(error_messages) + '\',' +
				'logs=\'' + str(logs) + '\',' +
				'start_execution_date=\'' + str(start_execution_date) + '\',' +
				'end_execution_date=\'' + str(end_execution_date) + '\',' +
				'created_at=\'' + str(created_at) + '\',' +
				'updated_at=\'' + str(updated_at) + '\',' +
				'created_by_id=' + str(created_by_id) + ',' +
				'storage_unit_id=' + str(storage_unit_id) + ' ' +
				'WHERE id=' + str(_id) + ';')
		query = query.replace('\'None\'', 'NULL')
		cur.execute(query)
		self.conn.commit()
		cur.close()
