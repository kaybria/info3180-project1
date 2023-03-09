from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

app = Flask(__name__)


db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app,db)

app.config.from_object(Config)
from app import views

