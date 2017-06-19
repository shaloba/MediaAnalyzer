__author__ = 'shaloba'
import sys
import os
from flask import Flask
import logger


sys.path.append(os.getcwd().replace('web_service', ''))
app = Flask(__name__, static_url_path='')
app.config.from_object('application.settings')
