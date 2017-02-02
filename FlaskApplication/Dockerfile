FROM ubuntu:14.04
MAINTAINER phuochoang

# Install necessary packages
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Copy file to /app directory on container
ADD ./FlaskApplication /app/
ADD ./requirements.txt /app/requirements.txt

# Install Flask 
WORKDIR /app
RUN pip install -r requirements.txt

# Define port that can be reached
EXPOSE 5000

# Start application
ENTRYPOINT ["python"]
CMD ["hello.py"]
