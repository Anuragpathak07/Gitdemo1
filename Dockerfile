# Use a newer Python version
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Install system dependencies first
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev py3-pip

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

# Set the entry point
ENTRYPOINT ["python"]
CMD ["app.py"]
