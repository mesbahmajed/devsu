#!/usr/bin/env python

import unittest
import requests
import json
import sys
import socket
import api

#firstarg = sys.argv.pop()

firstarg = 'bill'

method = socket.gethostname()

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://0.0.0.0:5000')
        self.assertEqual(response.json(), {'hello': 'world'})


class TestFlaskApi(unittest.TestCase):

    firstarg = ""

    def setUp(self):
        self.app = api.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/hello/'+firstarg)
        self.assertEqual(json.loads(response.get_data()),{'message': 'Hello ' + firstarg + ' from ' + method })




if __name__ == "__main__":

        unittest.main()
