FROM ubuntu
RUN mkdir /www
WORKDIR /www
COPY Pipfile /www/
COPY Pipfile.lock /www/

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN apt update
RUN apt upgrade
RUN apt install -y \
	python3 \
	python3-dev \
	gettext \
	python3-pip \
	sqlite3 

RUN pip3 install pipenv

#needs correct run
RUN pipenv install

ENV PYTHONUNBUFFERED 1
#change
COPY . /www/ 
EXPOSE 8000
