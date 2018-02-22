#!/usr/bin/env python
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
import socket


app = Flask(__name__)
api = Api(app)
method = socket.gethostname()
@app.route('/')
def api_root():
    return 'Welcome'


@app.route('/hello/<nameid>')
def api_name(nameid):

    names = {'john', 'steve', 'bill'}


    if nameid in names:
        return jsonify({'message': 'Hello ' + nameid + ' from ' + method})
    else:
        return  jsonify({'error' : 'Name is not correct'})

if __name__ == '__main__':
     app.run(host='0.0.0.0',port=5000)
