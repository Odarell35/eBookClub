#!/usr/bin/python3
"""Reviews models"""
from web_site import db
from web_site import models


class Reviews(db.Model):
    """reveiws class"""
    id = db.Column(db.Integer, primary_key=True, unique=True)
    Book_id = db.Column(db.String(60), db.ForeignKey("books.id"), nullable=False)
    Bookname = db.Column(db.String(60), db.ForeignKey("books.title"), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey("user.id"), nullable=False)
    username = db.Column(db.String(60), db.ForeignKey("user.name"), nullable=False)
    Review_text = db.Column(db.Text(1024), nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
