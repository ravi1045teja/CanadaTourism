from flask import request
from flask_restplus import Resource

from ..util.dto import TicketDto
from ..service.ticket_service import bookTicket,getTicket

api = TicketDto.api
_user = TicketDto.ticket


@api.route('/')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class UserList(Resource):
    @api.response(200, 'Ticket booked')
    @api.doc('Book ticket')
    @api.expect(_user, validate=True)
    def post(self):
        """Ticket booking """
        data = request.json
        auth_header = request.headers
        return bookTicket(data=data,headers=auth_header)

@api.route('/<ticketId>')
@api.param('ticketId', 'The ticket identifier')
@api.response(404, 'User not found.')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class GetPackage(Resource):
    @api.doc('get a package')
    @api.marshal_with(_user)
    def get(self, ticketId):
        """get ticket for a id"""
        package = getTicket(ticketId)
        if not package:
            api.abort(404)
        else:
            return package