FROM python:3
ENV PYTHONUNBUFFERED 1
run mkdir /workspace
WORKDIR /workspace
add requirements.txt /workspace/
RUN pip install -r requirements.txt
ADD . /workspace/
