# Zipcode Microservice

This microservice returns the zipcode for a given area.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

Clone the repository:
    
    ```bash
    git clone https://github.com/peng-shan/zipcode-microservice.git
    ```

Build the docker image:
    
    ```bash
    docker build -t zipcode-microservice .
    ```

Run the docker container:
    
    ```bash
    docker run -p 5000:5000 zipcode-microservice
    ```

# Weather Microservice

This microservice returns the weather for a given zipcode.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

Clone the repository:
    
    ```bash
    git clone https://github.com/peng-shan/weather-microservice.git
    ```

Build the docker image:
    
    ```bash
    docker build -t weather-microservice .
    ```

Run the docker container:
    
    ```bash
    docker run -p 5001:5001 weather-microservice
    ```

#Integration

client.py is a simple client that integrates the two microservices. It takes a zipcode as input and returns the weather for that zipcode.

##Running the client

    ```bash
    python client.py
    ```
    



