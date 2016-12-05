import psycopg2

class Connection():

	def __init__(self, host='127.0.0.1', port=5432, name='', user='', password=''):
		self.host = host
		self.port = port
		self.name = name
		self.user = user
		self.password = password

	def connect(self):
		conn_str = "dbname='%s' user='%s' host='%s' password='%s'"
		conn_str = conn_str % (self.name, self.user, self.host, self.password)
		self.curr_conn = psycopg2.connect(conn_str)
