from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

weathers = {
    '11111': {'temperature': 72, 'condition': 'Sunny'},
    '22222': {'temperature': 80, 'condition': 'Sunny'},
    '33333': {'temperature': 60, 'condition': 'Cloudy'}
}
class Weather(Resource):
    def get(self, zipcode):
        # Get weather information for the zipcode using a weather API
        if zipcode in weathers:
            return weathers[zipcode]
        else:
            return {'message': 'Zipcode not found'}, 404

api.add_resource(Weather, '/weather/<string:zipcode>')

if __name__ == '__main__':
    app.run(debug=True)
