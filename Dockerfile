# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

# Install dependencies
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy local code to the container image.
COPY . /app

# Set working directory
WORKDIR /app

# Run the web service on container startup.
ENTRYPOINT ["python", "app.py"]