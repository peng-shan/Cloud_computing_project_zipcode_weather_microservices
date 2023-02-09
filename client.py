import requests

def get_weather(area):
    url = f'http://localhost:5001/zipcode/{area}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    print(get_weather('Chicago'))

if __name__ == '__main__':
    main()
