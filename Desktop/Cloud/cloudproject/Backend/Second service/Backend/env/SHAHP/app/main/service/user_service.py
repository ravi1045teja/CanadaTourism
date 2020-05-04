import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.models import Userdetail
import smtplib, ssl
import math, random 


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    
    if not user :
        pub =str(uuid.uuid4())
        new_user = User(
            public_id=pub,
            email=data['email'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return add_user(data,pub)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return Userdetail.query.all()


def get_a_user(public_id):
    return Userdetail.query.filter_by(userId=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def add_user(data,pub):
    try:
        new_user= Userdetail(
            userId = pub,
            firstName =  data['firstName'],
            lastName =  data['lastName'],
            email =  data['email'],
            gender = data['gender'],
            phoneNo =  data['phoneNo']
        )

        save_changes(new_user)
        #mail()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'           
        }
        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def notifMail():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    password = "kutty007"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    server=smtplib.SMTP(smtp_server, port) 
    server.ehlo()  # Can be omitted
    server.starttls(context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

