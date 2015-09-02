import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	def __init__(self, email, password):
		self.email = email
		self.password = password

	

from app import endpoints



