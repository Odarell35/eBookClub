#!/usr/bin/python3
"""User model"""
from flask_login import UserMixin
from datetime import datetime
from web_site import db

class User(db.Model, UserMixin):
    """user class"""
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128), nullable=True)
    surname = db.Column(db.String(128), nullable=True)
    email = db.Column(db.String(128), nullable=True, unique=True)
    password = db.Column(db.String(128), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.now)

