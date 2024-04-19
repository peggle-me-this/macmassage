# Use the Python 3 base image
FROM python:3-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
