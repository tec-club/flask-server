from app import db

class User(db.Model):
	__table_args__ = {'extend_existing': True}

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	def __init__(self, email, password):
		self.email = email
		self.password = password
