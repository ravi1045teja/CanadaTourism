from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'firstName': fields.String(required=True, description='user username'),
        'lastName': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'phoneNo': fields.String(required=True, description='user phoneNo'),
        'gender': fields.String(required=True, description='user gender'),
        
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
        'otp': fields.String(required=False, description='otp'),
    })

class PackageDto:
    api = Namespace('package', description="package details")
    pack = api.model('package',{
        'packageId': fields.String(required=True, description='packageId'),
        'source': fields.String(required=True, description='source'),
        'destination': fields.String(required=True, description='destination'),
        'price': fields.String(required=True, description='price'),
        'transportMode': fields.String(required=True, description='transportMode')
       
    })
class LocationDto:
    api = Namespace('touristSpots', description="Tourist spot details")
    loc = api.model('touristSpots',{
        'id': fields.String(required=True, description='id'),
        'name': fields.String(required=True, description='name'),
        'location': fields.String(required=True, description='location'),
        'keyFeatures': fields.String(required=True, description='Key features'),
        'type': fields.String(required=True, description='transportMode'),
        'imagePath': fields.String(required=True, description='imagePath')
    })
class PaymentDto:
    api = Namespace('payment', description="Payment")
    
    tans = api.model('Payment', {
        'cardDetails': fields.String(required=True, description='Card details '),
        'public_id': fields.String(required=True, description='user public id'),
        'paymentMethod': fields.String(required=True, description='Payment Method')
    })

class TicketDto:
    api = Namespace('Ticket', description="ticket booking and details")
    ticket = api.model('ticket',{
        'transactionId': fields.String(required=True, description='packageId'),
        'packageId': fields.String(required=True, description='packageId'),
        'bookingUserId': fields.String(required=True, description='packageId'),
        'departing': fields.String(required=True, description='departing'),
        'returning': fields.String(required=True, description='returning'),
        'ticketPrice': fields.String(required=True, description='ticket Price'),
        'email': fields.String(required=True, description='email')
    })