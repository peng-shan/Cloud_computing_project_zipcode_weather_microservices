from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests

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
            zipcode = zipcodes[area]
            response = requests.get(f'http://weather-app:5000/weather/{zipcode}')
            if response.status_code == 200:
                return response.json()
            else:
                print("error: weather api not available")
                return {'error': 'Weather API not available'}, 503

            # return {area: zipcodes[area]}
        else:
            return {'error': 'Area not found'}, 404

api.add_resource(Zipcode, '/zipcode/<string:area>')

if __name__ == '__main__':
    app.run(debug=True)
