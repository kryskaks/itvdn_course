
import logging
# from logging.handlers import FileHandler

from flask.logging import default_handler
from flask import Flask

from config import LOGGER_CONFIG

app = Flask(__name__)

handler = logging.FileHandler('flask_app.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(LOGGER_CONFIG["formatter"])
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(LOGGER_CONFIG["formatter"])
app.logger.addHandler(ch)

app.logger.removeHandler(default_handler)

import views
