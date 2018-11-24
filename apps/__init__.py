from flask import Flask
app = Flask(__name__)

app.debug=True


from flask_sqlalchemy import SQLAlchemy

import os

from flask_login import LoginManager



loginmanager = LoginManager()
loginmanager.init_app(app)
login_manager=LoginManager(app)
login_manager.login_view = "login"
login_manager.session_protection = 'strong'

app.config['SECRET_KEY']='you-will-never-guess'
app.config['MAX_CONTENT_LENGTH']=2*1024*1024

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db=SQLAlchemy(app)

import apps.views
