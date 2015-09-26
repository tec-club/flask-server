from flask.ext.httpauth import HTTPBasicAuth
from flask import *
from app import app
from app import User
from app import db 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from datetime import date
import time
from app import Event
import json

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

	existentUser = User.query.filter_by(email=username).first()
	if existentUser:
		if existentUser.password == password:
			return jsonify(username = existentUser.email, password = existentUser.password)
		else:
			#username exists but invalid password
			return jsonify(error = "Invalid Password")
	else:
		if isValid(username, password) == True:
			#add user to DB
			user = User(username, password)
			db.session.add(user)
			db.session.commit()
			return jsonify(username = user.username, password = user.password)
		else:
			return jsonify(error = "Invalid Credentials")
def isValid(username, password):

	validCredentials = True

	driver = webdriver.Firefox()
	driver.get('https://cdm.schoolloop.com/portal/login?d=x&return_url=1441305916064')
	usernameField = driver.find_element_by_name("login_name")
	usernameField.send_keys(username)
	passwordField = driver.find_element_by_name("password")
	passwordField.send_keys(password)
	passwordField.send_keys(Keys.RETURN)
	try: 
		driver.find_element_by_name("message_header")
		driver.close()
		validCredentials = False
	except:
		validCredentials = True
		driver.close()

	return jsonify(result = validCredentials)


@app.route('/api/validLogin/', methods=['POST'])
def validLogin():

	username = request.json["username"]
	password = request.json["password"]

	print(request.json)
	print("user" + request.json.get("username"))
	validCredentials = True

	driver = webdriver.Firefox()
	driver.get('https://cdm.schoolloop.com/portal/login?d=x&return_url=1441305916064')
	usernameField = driver.find_element_by_name("login_name")
	usernameField.send_keys(username)
	passwordField = driver.find_element_by_name("password")
	passwordField.send_keys(password)
	passwordField.send_keys(Keys.RETURN)
	try: 
		driver.find_element_by_name("message_header")
		driver.close()
		validCredentials = False
	except:
		validCredentials = True
		driver.close()

	return jsonify(result = validCredentials)

def getEvents():

	baseURL = 'http://cdm.nmusd.us/cms/month?d=x&group_id=1204427108703&month_id=0&return_url=1441484418787'
	page = requests.get(baseURL)

	soup = BeautifulSoup(page.content)

	results = soup.findAll("a", {"name":"Event Details"})

	calendarEvents = []

	for event in results:
		if event.has_attr('href'):
			url = event.get('href') #from event tag
			detailsPage = requests.get('http://cdm.nmusd.us'+url)
			detailsSoup = BeautifulSoup(detailsPage.content)
			date = detailsSoup.find("div", class_="date")
			d=date.findAll(text=True)

			dateSplit = str(d)[3:len(str(d))-2]


			rawTitle = event.findAll(text=True)

			#properly formatted title
			titleSplit = str(rawTitle)[2:len(str(rawTitle))-1]

			eventObj = Event(titleSplit, dateSplit)

			#make date object from calendar event
			date = time.strptime(dateSplit, "%m/%d/%y")
			
			#get timestamp of date object and compare it to the current time
			if (time.mktime(date) > time.time()):
				#serialize the events object and append it to array
				calendarEvents.append(eventObj.to_Dic())
	return calendarEvents

#Retreive upcoming news or announcements
@app.route('/api/events')
def getAnnouncements():

	calendarEvents = getEvents()

	return jsonify(events = calendarEvents)

#Retreive the next late start date from the current date
@app.route('/api/late_start/next_date')
def getNextday():
	upcomingEvents = getEvents()

	for event in upcomingEvents:
		if event['title'] == "Late Start":
			return jsonify(late_start=event)

	return ""




