import requests

def get_weather(area):
    zipcode_url = f'http://localhost:5000/zipcode/{area}'
    r = requests.get(zipcode_url)
    if r.status_code == 200:
        zipcode = r.json()[area]
        weather_url = f'http://localhost:5001/weather/{zipcode}'
        r = requests.get(weather_url)
        if r.status_code == 200:
            return r.json()
        else:
            return {'error': 'Error getting weather information'}
    else:
        return {'error': 'Area not found'}

def main():
    print(get_weather('New York'))

if __name__ == '__main__':
    main()
