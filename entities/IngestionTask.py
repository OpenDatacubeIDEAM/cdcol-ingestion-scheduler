import dao.IngestTask as DAOIngestTask

class IngestionTask():

	STATES= {
			'SCHEDULED_STATE':'1',
			'EXECUTING_STATE':'2',
			'FAILED_STATED':'3',
			'COMPLETED_STATE':'4'
			}

	def __init__(self, dao_itask):
		
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

