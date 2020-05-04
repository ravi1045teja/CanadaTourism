from app.main import db
from app.main.model.models import Ticket
import uuid
import requests

import smtplib, ssl
def bookTicket(data,headers):
    response = requests.get('http://localhost:5001/auth/validate', headers=headers)
    rj = response.json()
    print(rj['status'])
    if(str(rj['status']) == 'success'):
        pub =str(uuid.uuid4())
        ticket =  Ticket(
        ticketId = pub,
        transactionId = data['transactionId'],
        packageId = int(data['packageId']),
        bookingUserId = data['bookingUserId'],
        ticketPrice =data['ticketPrice'],
        departing = data['departing'],
        returning = data['returning'],
        email = data['email']
        )
        mail(data['email'],pub)
        save_changes(ticket)
        response_object = {
            'status': 'success',
            'message': 'Successfully Payment made.',
            'ticketId' :  pub          
        }
        return response_object,200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Token error',
                    
        }
        return response_object,200

def getTicket(ticketId):
     return Ticket.query.filter_by(ticketId=ticketId).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def mail(email,ticketId):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "hariarunachalam27@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "ynwmrwprdnbhihwh"
    message = """\
    Subject: Tourism for All

    your Ticket id: """+ ticketId

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port) 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)