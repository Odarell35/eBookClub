#!/usr/bin/python3
"""Category model"""
from web_site import db
from web_site import models
from .Books_model import Books

class Category(db.Model):
    """category class with f.f attr
    category number, name
    """
    id = db.Column(db.Integer, primary_key=True, unique=True)
    category_name = db.Column(db.String(128), nullable=False)
    books = db.relationship('Books', backref='category')
