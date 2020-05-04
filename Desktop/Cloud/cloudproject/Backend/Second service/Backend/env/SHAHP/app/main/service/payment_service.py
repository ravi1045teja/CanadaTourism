from app.main import db
from app.main.model.models import Transaction
import uuid
import requests


def doTransaction(data,headers):
    response = requests.get('http://localhost:5001/auth/validate', headers=headers)
    rj = response.json()
    print(rj['status'])
    if(str(rj['status']) == 'success'):
        pub =str(uuid.uuid4())
        trans =  Transaction(
        transactionId = pub,
        paymentMethod = "credit",
        transactionSuccess = "success",
        userId = data['public_id'],
        cardDetails = data['cardDetails']
        )
        save_changes(trans)
        response_object = {
            'status': 'success',
            'message': 'Successfully Payment made.',
            'transactionId' :  pub          
        }
        return response_object,200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Token error',
                    
        }
        return response_object,200
    


def save_changes(data):
    db.session.add(data)
    db.session.commit()
