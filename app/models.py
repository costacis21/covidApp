from app import db
from datetime import datetime

# class of user used for the db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    status = db.Column(db.String(100))
    dateTime = db.Column(db.DateTime, nullable=False)