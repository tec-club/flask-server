from app import db

class User(db.Model):
	__table_args__ = {'extend_existing': True}

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(120))

	def __init__(self, email, password):
		self.email = email
		self.password = password



class SchoolloopClass(db.Model):
	__table_args__={'extend_existing': True}
	id= db.Column(db.Integer, primary_key=True)
	course=db.Column(db.String(120))
	teacher=db.Column(db.String(80))
	grade=db.Column(db.Float(1000, True)) #Not 100% sure on precision (1st) parameter
	period=db.Column(db.Integer)

	#Creates many to one link between schoolloopclass and User
	user=relationship("User", backref=backref("classes", order_by=id))
	def __init__(self, course, teacher, grade, period):
		self.course=course;
		self.teacher=teacher;
		self.grade=grade;
		self.period=period;

class SchoolloopAssignment(db.Model):
	__table_args__={'extend_existing': True}
	id=db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(120))
	score=db.Column(db.String(10))  #Scores stored in strings to preserve weighting.i.e 70/100vs7/10
	#creates relationship between SchoolloopClass and SchoolloopAssignment
	schoolloopclass=relationship("SchoolloopClass", backref=backref("assignments", order_by=id))

	def __init__(self, title, score):
		self.title=title
		self.score=score