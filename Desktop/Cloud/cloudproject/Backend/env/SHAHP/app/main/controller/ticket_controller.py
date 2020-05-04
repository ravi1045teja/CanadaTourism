from flask import request
from flask_restplus import Resource

from ..util.dto import TicketDto
from ..service.ticket_service import bookTicket,getTicket

api = TicketDto.api
_ticket = TicketDto.ticket


@api.route('/')
class BookTicket(Resource):
   
    @api.response(200, 'Ticket booked')
    @api.doc('Book ticket')
    @api.expect(_ticket, validate=True)
    def post(self):
        """Ticket booking """
        data = request.json
        return bookTicket(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The ticket identifier')
@api.response(404, 'User not found.')
class getTickets(Resource):
    @api.doc('get a package')
    @api.marshal_list_with(_ticket)
    def get(self, public_id):
        """get ticket for a id"""
        package = getTicket(public_id)
        if not package:
            api.abort(404)
        else:
            return package