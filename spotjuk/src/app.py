from flask import Flask

from src.blueprints import views

app = Flask(__name__)

views.init_app(app)