from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto,UserResponseDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user
_userResponse = UserDto.userR
ap = UserResponseDto.api

@api.route('/')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class UserList(Resource):
    @api.doc('list_of_registered_students')
    @api.marshal_list_with(_userResponse, envelope='data')
    def get(self):
        """List all registered users"""
        auth_header = request.headers.get('Authorization')
        return get_all_users(data=auth_header)

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_userResponse)
    def get(self, public_id):
        """get a user given its identifier"""
        auth_header = request.headers.get('Authorization')
        user = get_a_user(public_id,data=auth_header)
        if not user:
            api.abort(404)
        else:
            return user