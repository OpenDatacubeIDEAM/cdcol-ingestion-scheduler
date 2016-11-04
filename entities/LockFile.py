import os

class LockFile():

	def __init__(self, pid_file_path):
		self.pid_file = pid_file_path
	
	def search(self):
		if os.path.exists(self.pid_file):
			return True
		else:
			return False

	def write(self):
		with open(self.pid_file, 'w') as pid_file:
			pid_file.write(str(os.getpid()))

	def delete(self):
		os.remove(self.pid_file)
