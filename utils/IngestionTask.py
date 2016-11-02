from ConfigParser import ConfigParser
from datetime import datetime
import os

class IngestionTask():
	
	def __init__(self, stg_unit_name, task_path):
		self.stg_unit_name = stg_unit_name
		self.task_path = task_path
		self.conf_file = task_path + '/task.conf' 
		self.create_config()

	def create_config(self):
		if not os.path.exists(self.conf_file):
			self.conf = ConfigParser()
			self.conf.add_section('info')
			self.conf.set('info', 'status', 'pending')
			self.conf.set('info', 'storage unit name', self.stg_unit_name)
			self.conf.set('info', 'task path', self.task_path)
			self.conf.set('info', 'last update', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		
			with open(self.conf_file, 'wb') as conf_file:
				self.conf.write(conf_file)
		else:
			self.conf = ConfigParser()
			self.conf.read(self.conf_file)

