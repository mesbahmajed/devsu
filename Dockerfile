# Format: FROM    repository[:version]
FROM       ubuntu:latest
FROM       python:2.7

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD api.py /

RUN pip install pystrich
RUN pip install flask flask-jsonpify flask-restful
RUN pip freeze
CMD [ "python", "./api.py" ]


