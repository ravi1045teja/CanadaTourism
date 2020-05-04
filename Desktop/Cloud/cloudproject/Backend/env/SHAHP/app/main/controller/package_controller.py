from flask import request
from flask_restplus import Resource

from ..util.dto import PackageDto
from ..service.package_service import get_all_packages,search_packages,get_a_package

api = PackageDto.api
_package = PackageDto.pack

@api.route('/')
class PackageList(Resource):
    @api.doc('list_of_packages')
    @api.marshal_list_with(_package, envelope='data')
    def get(self):
        """list all packages"""
        return get_all_packages()

@api.route('/<search_word>')
@api.param('search_word', 'The User identifier')
@api.response(404, 'User not found.')
class GetPackage(Resource):
    @api.doc('get a package')
    @api.marshal_with(_package)
    def get(self, search_word):
        """get packages for a destination"""
        packages = search_packages(search_word)
        if not packages:
            api.abort(404)
        else:
            return packages