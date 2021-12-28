from flask import Flask

from src.ext import database
from src.blueprints import views

app = Flask(__name__)

database.init_app(app)
views.init_app(app)