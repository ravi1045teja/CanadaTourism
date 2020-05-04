from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kutty007'
app.config['MYSQL_DB'] = 'jobreport'

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
     app.run(port=5002)
