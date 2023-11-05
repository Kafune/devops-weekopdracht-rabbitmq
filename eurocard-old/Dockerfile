# Set the base image. 
FROM python:3.8

# Sets the user name to use when running the image.
USER root

# Update the package list and install necessary packages
RUN apt-get update && apt-get install -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Make a directory for our app
WORKDIR /eurocard

# Copy the requirements file into the container at /eurocard
COPY requirements.txt /eurocard/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container at /eurocard
COPY eurocard.py /eurocard/

# Run the application
CMD ["python", "/eurocard/eurocard.py"]
