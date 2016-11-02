from IngestionTask import IngestionTask
import os

class IngestionTasks():

	tasks = {}

	def search_tasks(self, stg_units_path):

		stg_units = [x for x in os.listdir(stg_units_path) if os.path.isdir(stg_units_path + '/' + x)] 

		for stg_unit in stg_units:
			stg_unit_folder = stg_units_path + '/' + stg_unit
			ing_tasks = [x for x in os.listdir(stg_unit_folder) if os.path.isdir(stg_unit_folder + '/' + x)]
			
			for task in ing_tasks:
				if stg_unit not in self.tasks:
					self.tasks[stg_unit] = []
				self.tasks[stg_unit].append(IngestionTask(stg_unit, stg_unit_folder + '/' + task))


