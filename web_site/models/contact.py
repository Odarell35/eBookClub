#!/usr/bin/pyhton3
"""Books Model"""
from web_site import db
from web_site import models

class Contact_us(db.Model):
    """contact us"""
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    phone_number = db.Column(db.Integer)
    message_box = db.Column(db.String(1024), nullable=False)
