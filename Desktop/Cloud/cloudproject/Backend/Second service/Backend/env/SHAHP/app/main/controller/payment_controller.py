from flask import request
from flask_restplus import Resource

from ..util.dto import PaymentDto
from ..service.payment_service import doTransaction

api = PaymentDto.api
_user = PaymentDto.tans


@api.route('/')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class UserList(Resource):
   
    @api.response(200, 'Payment Done')
    @api.doc('Do payment')
    @api.expect(_user, validate=True)
    def post(self):
        """Payment """
        data = request.json
        auth_header = request.headers
        return doTransaction(data=data,headers=auth_header)