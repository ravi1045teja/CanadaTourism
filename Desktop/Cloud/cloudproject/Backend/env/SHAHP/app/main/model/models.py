# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from .. import db




# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

from .. import db

class Package(db.Model):
    __tablename__ = 'package'
    __bind_key__ ='users'
    packageId = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(45))
    destination = db.Column(db.String(45))
    price = db.Column(db.Integer)
    transportMode = db.Column(db.String(45))



class Ticket(db.Model):
    __tablename__ = 'ticket'
    __bind_key__ = 'users'
    ticketId = db.Column(db.String(100), primary_key=True)
    transactionId = db.Column(db.String(100), nullable=False)
    packageId = db.Column(db.Integer,nullable=False)
    bookingUserId = db.Column(db.String(100), nullable=False)
    ticketPrice = db.Column(db.Integer)
    departing = db.Column(db.String(45))
    returning = db.Column(db.String(45))
    email = db.Column(db.String(100))

class Transaction(db.Model):
    __tablename__ = 'transaction'
    __bind_key__ = 'users'
    transactionId = db.Column(db.String(100), primary_key=True)
    paymentMethod = db.Column(db.String(45))
    transactionSuccess = db.Column(db.String(45))
    userId = db.Column(db.String(100))
    cardDetails = db.Column(db.String(45))

class Userdetail(db.Model):
    __tablename__ = 'userdetails'
    __bind_key__ = 'users'
    userId = db.Column(db.String(100), primary_key=True)
    firstName = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    email = db.Column(db.String(45))
    phoneNo = db.Column(db.String(45))

class TouristSpots(db.Model):
    __tablename__ = 'touristspots'
    __bind_key__ = 'users'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(45))
    location = db.Column(db.String(45))
    keyFeatures = db.Column(db.String(45))
    type = db.Column(db.String(45))
    imagePath = db.Column(db.String(200))

