# Set base image (host OS)
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy all files to the working folder
COPY . .

# By default, listen on port 5000
EXPOSE 5000

CMD ["gunicorn","--timeout","90","--bind","0.0.0.0:5000","wsgi:app"]

