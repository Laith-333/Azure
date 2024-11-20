# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install required packages
RUN apt-get update && apt-get install -y nginx && apt-get clean

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Create app directory
WORKDIR /app

# Copy the application code
COPY app/ /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Nginx configuration
COPY app/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx and the application
CMD ["bash", "-c", "nginx && python app.py"]
