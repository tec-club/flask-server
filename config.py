import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = "cdmhs2015asb"