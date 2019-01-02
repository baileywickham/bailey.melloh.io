FROM ubuntu
RUN mkdir /www
WORKDIR /www
COPY Pipfile /www/
COPY Pipfile.lock /www/

ENV PYTHONUNBUFFERED 1

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN apt update
RUN apt upgrade -y
RUN apt install -y \
	python3 \
	python3-dev \
	gettext \
	python3-pip \
	sqlite3 

RUN pip3 install pipenv
RUN pipenv install --system --deploy 

#change
COPY . /www/ 
WORKDIR /www/bailey
RUN python3 manage.py collectstatic --noinput
EXPOSE 8000
