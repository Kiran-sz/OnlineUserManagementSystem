
FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1

ENV ALLOWED_HOST *

RUN apt update                              \
    && apt install -y python3.8             \
    && apt install -y python3-pip           \
    && apt install -y libmysqlclient-dev

# create root directory for our project in the container
RUN mkdir /MyRestService

WORKDIR /MyRestService
# Copy the website build from built to docker and re-arrenge for running
ADD ./build/lib/ /MyRestService/
RUN mv ./restWebsite/HRM .

# Add and Install packages required with docker only
ADD requirements_prod.txt /MyRestService/
RUN python3 -m pip install -r requirements_prod.txt


EXPOSE 8000/tcp
CMD exec python3 -m gunicorn restWebsite.wsgi:application -b '[::]:8000'

