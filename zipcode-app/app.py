from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

zipcodes = {
    'New-York': '11111',
    'Los-Angeles': '22222',
    'Chicago': '33333'
}

class Zipcode(Resource):
    def get(self, area):
        if area in zipcodes:
            return {area: zipcodes[area]}
        else:
            return {'error': 'Area not found'}, 404

api.add_resource(Zipcode, '/zipcode/<string:area>')

if __name__ == '__main__':
    app.run(debug=True)
