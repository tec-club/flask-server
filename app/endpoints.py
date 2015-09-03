from flask.ext.httpauth import HTTPBasicAuth
from flask import *
from app import app
from app import User
from app import db 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

auth = HTTPBasicAuth()


#authenticate by retreiving a password
@auth.get_password
def get_password(email):
	user = User.query.filter_by(email=email).first()

	if user:
		return user.password
	return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'unauthorized'}), 401)


@app.route('/')
@app.route('/index')
def index():
	user = User.query.filter_by(email='student11').first()
	print(user)
	return "Hello, world!"

# verify the credentials work with school loop
@app.route('/api/signIn/', methods=['POST'])
def signIn():
	username = request.values.get("username")
	password = request.values.get("password")
	existentUser = User.query.filter_by(email=username, password=password).first()
	if existentUser:
		return jsonify(username = existentUser.email, password = existentUser.password)
	else:
		if validLogin(username, password) == True:
			#add user to DB
			user = User(username, password)
			db.session.add(user)
			db.session.commit()
			return jsonify(username = user.username, password = user.password)

def validLogin(username, password):

	validCredentials = True

	driver = webdriver.Firefox()
	driver.get('https://cdm.schoolloop.com/portal/login?d=x&return_url=1441305916064')
	usernameField = driver.find_element_by_name("login_name")
	usernameField.send_keys("chersowitz")
	passwordField = driver.find_element_by_name("password")
	passwordField.send_keys("c10395009009")
	passwordField.send_keys(Keys.RETURN)
	try: 
		driver.find_element_by_name("message_header")
		driver.close()
		validCredentials = False
	except:
		validCredentials == True
		driver.close()

	return validCredentials

#Retreive the next late start date from the current date
@app.route('/api/late_start/next_date')
def getNextday():
	return "Monday August 14"

#Retreive upcoming news or announcements
@app.route('/api/announcements')
def getAnnouncements(announcements):
	return "announcements"