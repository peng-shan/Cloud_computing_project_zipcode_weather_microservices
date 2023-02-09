docker build -t zipcode-app:latest .
docker run -p 5001:5000 --name zipcode-app --network n1 --hostname zipcode-app --ip 172.20.0.4 zipcode-app