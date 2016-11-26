class StorageUnit():

	def __init__(self, dao_stg_unit):
	
		self._id = dao_stg_unit['id']
		self.name = dao_stg_unit['name']
		self.description = dao_stg_unit['description']
		self.description_file = dao_stg_unit['description_file']
		self.ingest_file = dao_stg_unit['ingest_file']
		self.metadata = dao_stg_unit['metadata']
		self.root_dir = dao_stg_unit['root_dir']
		self.created_at = dao_stg_unit['created_at']
		self.updated_at = dao_stg_unit['updated_at']
		self.created_by_id = dao_stg_unit['created_by_id']
		self.metadata_generation_script = dao_stg_unit['metadata_generation_script']
