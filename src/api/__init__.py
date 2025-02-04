from flask import Flask
from ..config import Config

app = Flask(__name__, 
           static_folder=Config.STATIC_DIR,
           template_folder=Config.TEMPLATE_DIR)

from . import routes
