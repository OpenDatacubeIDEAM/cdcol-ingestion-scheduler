from dao.IngestTask import IngestTask as DAOIngestTask
import datetime

class IngestionTask():

	STATES= {
			'SCHEDULED_STATE':'1',
			'EXECUTING_STATE':'2',
			'FAILED_STATE':'3',
			'COMPLETED_STATE':'4'
			}

	def __init__(self, dao_itask, conn=None):

		self.conn = conn
		self._id = dao_itask['id']
		self.state = dao_itask['state']
		self.comments = dao_itask['comments']
		self.error_messages = dao_itask['error_messages']
		self.logs = dao_itask['logs']
		self.start_execution_date = dao_itask['start_execution_date']
		self.end_execution_date = dao_itask['end_execution_date']
		self.created_at = dao_itask['created_at']
		self.updated_at = dao_itask['updated_at']
		self.created_by_id = dao_itask['created_by_id']
		self.storage_unit_id = dao_itask['storage_unit_id']

	def save(self):

		self.updated_at = str(datetime.datetime.now())

		dao_itask = DAOIngestTask(self.conn)
		dao_itask.update(self._id,
						self.state,
						self.comments,
						self.error_messages,
						self.logs,
						self.start_execution_date,
						self.end_execution_date,
						self.created_at,
						self.updated_at,
						self.created_by_id,
						self.storage_unit_id
						)
