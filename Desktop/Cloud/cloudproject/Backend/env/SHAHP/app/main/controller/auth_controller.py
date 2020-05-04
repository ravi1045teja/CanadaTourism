from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)

@api.route('/loginSecond')
class UserLoginSecond(Resource):
    """
        User Login Resource
    """
    @api.doc('user login with otp')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user_with_otp(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)

@api.route('/validate')
@api.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
class validate(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    # @api.marshal_with(user_det, envelope='data')
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.get_logged_in_user(new_request=auth_header)