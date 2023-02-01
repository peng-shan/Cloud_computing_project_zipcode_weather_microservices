# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

# Set the environment variable
ENV FLASK_APP=app.py

# Expose the default port for Flask
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
