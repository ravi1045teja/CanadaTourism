# coding: utf-8
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Package(db.Model):
    __tablename__ = 'package'

    packageId = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(45))
    destination = db.Column(db.String(45))
    price = db.Column(db.Integer)
    transportMode = db.Column(db.String(45))



class Ticket(db.Model):
    __tablename__ = 'ticket'

    ticketId = db.Column(db.Integer, primary_key=True)
    packageId = db.Column(db.Integer)
    bookingUserId = db.Column(db.Integer, nullable=False)
    ticketPrice = db.Column(db.Integer)
    dicountPriceApplied = db.Column(db.Integer)



class Transaction(db.Model):
    __tablename__ = 'transaction'

    transactionId = db.Column(db.Integer, primary_key=True)
    paymentMethod = db.Column(db.String(45))
    transactionSuccess = db.Column(db.String(45))
    ticketId = db.Column(db.String(45))



class Userdetail(db.Model):
    __tablename__ = 'userdetails'

    userId = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(45))
    lastName = db.Column(db.String(45))
    gender = db.Column(db.String(45))
    email = db.Column(db.String(45))
    phoneNo = db.Column(db.String(45))
