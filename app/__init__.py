from flask import flask
from flask_sqlachemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevConfig")

db = SQLAlchemy(app)

from app import routes