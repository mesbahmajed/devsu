FROM python:2.7

ADD api.py /

RUN pip install pystrich
RUN pip install flask flask-jsonpify flask-restful
RUN pip freeze
CMD [ "python", "./api.py" ]
