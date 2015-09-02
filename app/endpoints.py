from flask.ext.httpauth import HTTPBasicAuth
from flask import *
from app import app
auth = HTTPBasicAuth()


#authenticate by retreiving a password
@auth.get_password
def get_password(email):
	if email == 'test@gmail.com':
		return 'password'
	return none


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'unauthorized'}), 401)


@app.route('/')
@app.route('/index')
def index():
	return "Hello, world!"


#Retreive the next late start date from the current date
@app.route('/api/late_start/next_date')
def getNextday():
	return "Monday August 14"

#Retreive upcoming news or announcements
@app.route('/api/announcements')
def getAnnouncements(announcements):
	return "announcements"