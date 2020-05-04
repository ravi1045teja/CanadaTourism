from app.main.model.user import User
from ..service.blacklist_service import save_token
import smtplib, ssl
import math, random 
from app.main import db
import string  
class Auth:


    @staticmethod
    def login_user_with_otp(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.otp == data.get('otp'):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Otp wrong'
                }
                return response_object, 200

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                #auth_token = user.encode_auth_token(user.id)
                otp = generateOTP()
                if otp:
                    user.otp = str(otp)
                    db.session.commit()
                    mail(data.get('email'),otp)
                    response_object = {
                        'status': 'success',
                        'message': 'OTP generated',
                        #'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 200

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        print("data"+data)
        if data:
            #print(data)
            auth_token = data.split(" ")[1]
            print(auth_token)
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
    
    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        if new_request:
            auth_token =new_request.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'public_id': user.public_id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

def mail(email,otp):
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "hariarunachalam27@gmail.com"  # Enter your address
    receiver_email = email  # Enter receiver address
    password = "ynwmrwprdnbhihwh"
    message = """\
    Subject: Tourism for All

    your otp: """+ otp

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port) 
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

def generateOTP() : 
  
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        ran = int(math.floor(random.random() * 10))
        OTP += digits[ran] 
  
    return OTP 