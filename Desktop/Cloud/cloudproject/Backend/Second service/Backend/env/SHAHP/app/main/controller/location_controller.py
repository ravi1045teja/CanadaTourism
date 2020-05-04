from flask import request
from flask_restplus import Resource

from ..util.dto import LocationDto
from ..service.location_service import get_all_locations,get_a_location

api = LocationDto.api
_loc = LocationDto.loc

@api.route('/')
class LocationList(Resource):
    @api.doc('list_of_packages')
    @api.marshal_list_with(_loc, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_locations()

@api.route('/<id>')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class GetPackage(Resource):
    @api.doc('get a package')
    @api.marshal_with(_loc)
    def get(self, id):
        """get packages for a destination"""
        package = get_a_location(id)
        if not package:
            api.abort(404)
        else:
            return package