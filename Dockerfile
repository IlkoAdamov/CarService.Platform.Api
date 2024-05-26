# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11.1

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

ARG VERSION_SUFFIX
ENV VERSION_SUFFIX=${VERSION_SUFFIX:-buildNumberUnsupplied}
RUN echo "Build number: $VERSION_SUFFIX"

# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /car_service_platform_api

# Get the Real World example app
#RUN git clone https://github.com/gothinkster/django-realworld-example-app.git /drf_src

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /car_service_platform_api

# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /car_service_platform_api

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]