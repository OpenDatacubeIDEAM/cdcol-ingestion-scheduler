class IngestionTask():
	
	def __init__(self, _id, state, errors, start_date,  end_date, updated_at, stg_unit_id):
		self._id = _id
		self.state = state
		self.errors = errors
		self.start_execution_date= start_date
		self.end_execution_date = end_date
		self.updated_at = updated_at
		self.storage_unit_id= stg_unit_id

	def __init__(self, dao_itask):
		
		self._id = dao_itask['id']
		self.state = dao_itask['state']
		self.errors = dao_itask['errors']
		self.start_execution_date = dao_itask['start_execution_date']
		self.end_execution_date = dao_itask['end_execution_date']
		self.updated_at = dao_itask['updated_at']
		self.storage_unit_id = dao_itask['storage_unit_id']
