from flask import *
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'about':'helloworld'}
    def post(self):
        some_json = request.get_json()
        return {'You sent': some_json}, 201
class Multi(Resource):
    def get(self,num):
        return {'result':num*10}

api.add_resource(Helloworld,'/')
api.add_resource(Multi,'/Multi/<int:num>')







if __name__=='__main__':
    app.run(debug=True)