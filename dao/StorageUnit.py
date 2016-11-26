from psycopg2.extensions import connection
from psycopg2.extras import DictCursor

class StorageUnit():

	def __init__(self, connection):
		self.conn = connection

	def get_by_id(self, stg_unit_id):
		cur = self.conn.cursor(cursor_factory=DictCursor)
		cur.execute('SELECT ' +
					'id, ' +
					'name, ' +
					'description, ' +
					'description_file, ' +
					'ingest_file, ' +
					'metadata, ' +
					'root_dir, ' +
					'created_at, ' +
					'updated_at, ' +
					'created_by_id, ' +
					'metadata_generation_script ' +
					'FROM storage_storageunit ' +
					'WHERE id=' + str(stg_unit_id) + ';')
		row = cur.fetchone()
		return row
