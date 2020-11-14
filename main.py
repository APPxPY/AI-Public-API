from flask import Flask
from flask_ssl import *
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

if __name__ == '__main__':
	# if ENABLE_HTTPS:
	# 	generator.SSLGenerator.generate_cert()
	# 	app.run(host=HOST, port=PORT, debug=DEBUG, ssl_context=(CERT_FILE, KEY_FILE))
	# else:
	app.run(host=HOST, port=PORT, debug=DEBUG)