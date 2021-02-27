from flask import Flask
from logging.handlers import RotatingFileHandler
from logging import Formatter
import logging

from env import *
from audio_processing import *
from image_processing import *
# from ssl_gen import generator
from log import log_stream

app = Flask(__name__)

if DEBUG:
	log_stream = log_stream.LogStream()
	logging.basicConfig(stream=log_stream, level=logging.DEBUG)

	@app.route('/log')
	def info_page():
		return f'{log_stream}'


@app.route('/api/processImage')
def image_process():
	pass
	
if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)