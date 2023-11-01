# Select base image
FROM python:3

# Install any operating system junk

# Set the working directory
WORKDIR /app

# Copy all the code from the local directory into the image
COPY planner planner
COPY goals goals
COPY tasks tasks
COPY common common

# Install dependencies
RUN pip install -r requirements.txt

# Set the command to run the application
CMD gunicorn --bind 0.0.0.0:8000 planner.wsgi
