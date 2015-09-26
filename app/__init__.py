import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify
import json

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

class Event():
	title=""
	date=""

	def __init__(self, title, date):
		self.date = date
		self.title = title

	def to_Dic(self):
		return {'title':str(self.title)[1:len(str(self.title))-1], 'date':self.date}

from app import endpoints



