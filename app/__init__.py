import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	def __init__(self, email, password):
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %s>' % self.email

	

from app import endpoints



