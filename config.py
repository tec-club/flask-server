import os
basedir = os.path.abspath(os.path.dirname(__file__))

"""SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_REPO = os.path.join(basedir, 'db_repository')"""
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = "cdmhs2015asb"