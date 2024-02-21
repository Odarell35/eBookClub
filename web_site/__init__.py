#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

DB = 'eBook_db.db'

app = Flask(__name__)
app.secret_key = 'key_0624191673'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['DEBUG'] = True
app.config['SESSION_COOKIE_SECURE'] = True

db = SQLAlchemy(app)
