from entities.IngestionTask import IngestionTask
from dao.IngestTask import IngestTask as DAOIngestTask
import os

class IngestionTasks():

	tasks = {}

	def __init__(self, conn):
		self.conn = conn

	def load_scheduled(self):
		dao_itask = DAOIngestTask(self.conn)
		for each_row in dao_itask.get_by_state(IngestionTask.STATES['SCHEDULED_STATE']):
			itask = IngestionTask(each_row, conn=self.conn)
			if each_row['storage_unit_id'] in self.tasks:
				self.tasks[each_row['storage_unit_id']].append(itask)
			else:
				self.tasks[each_row['storage_unit_id']] = [itask]
