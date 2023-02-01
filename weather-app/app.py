from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self, zipcode):
        zipcode_url = f'http://zipcode-microservice:5000/zipcode/{zipcode}'
        r = requests.get(zipcode_url)
        if r.status_code == 200:
            area = r.json()[zipcode]
            # Get weather information for the area using a weather API
            weather = {'area': area, 'temperature': 72, 'condition': 'Sunny'}
            return weather
        else:
            return {'error': 'Zipcode not found'}, 404

api.add_resource(Weather, '/weather/<string:zipcode>')

if __name__ == '__main__':
    app.run(debug=True)
