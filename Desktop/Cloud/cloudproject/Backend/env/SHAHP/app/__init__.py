
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.package_controller import api as pack_ns
from .main.controller.location_controller import api as loc_ns
from .main.controller.payment_controller import api as pay_ns
from .main.controller.ticket_controller import api as ticket_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
# api.add_namespace(pack_ns, path='/package')
# api.add_namespace(loc_ns, path='/location')
# api.add_namespace(pay_ns, path='/payment')
# api.add_namespace(ticket_ns, path='/ticket')