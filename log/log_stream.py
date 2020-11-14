import re
from ansi2html import Ansi2HTMLConverter

class LogStream(object):
	def __init__(self):
		self.logs = ''
		self.conv = Ansi2HTMLConverter()


	def write(self, str):
		self.logs += self.conv.convert(str)

	def flush(self):
		pass

	def __str__(self):
		return self.logs