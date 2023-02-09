docker build -t weather-app:latest .
docker run -p 5002:5000 --name weather-app --network n1 --hostname weather-app --ip 172.20.0.2 weather-app