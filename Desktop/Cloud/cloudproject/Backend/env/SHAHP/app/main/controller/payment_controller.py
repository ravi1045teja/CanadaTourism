from flask import request
from flask_restplus import Resource

from ..util.dto import PaymentDto
from ..service.payment_service import doTransaction

api = PaymentDto.api
_user = PaymentDto.tans


@api.route('/')
class UserList(Resource):
   
    @api.response(200, 'Payment Done')
    @api.doc('Do payment')
    @api.expect(_user, validate=True)
    def post(self):
        """Payment """
        data = request.json
        return doTransaction(data=data)