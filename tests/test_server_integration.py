import unittest
from http.server import HTTPServer
import urllib.request
from server.server_controller import HTTPServer_RequestHandler
import json
import _thread
import time
import os

SERVER_PORT = 5000



class TestServerIntegration(unittest.TestCase):
    is_server_ready = False

    @classmethod
    def sendRequest(cls,input,state=None):
        url='http://localhost:5000/calculate'
        if state:
            request_json = json.dumps({"calculatorState": state, "input": str(input)})
        else:
            request_json = json.dumps({"input": str(input)})
        binary=request_json.encode('utf8')
        request = urllib.request.Request(url,binary,{'Content-Type': 'application/json','Content-Length':len(request_json)})
        response = urllib.request.urlopen(request)
        #print("got from server: "+str(response.read()))
        body=response.read()
        body = body.decode('utf8')
        data = json.loads(body)
        return data

    @classmethod
    def setUpClass(cls):
        print("aaaaaaaaaaaaaa")
        _thread.start_new_thread(cls.powerup_server,())
        time.sleep(1)


    @classmethod
    def powerup_server(cls):
        print('starting test server...')
        server_address = ('0.0.0.0', SERVER_PORT)
        httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
        print('running server...')
        print('running on port ...' + str(SERVER_PORT))
        httpd.serve_forever()

    def test_sending_empty_state(self):
        response = self.sendRequest(2)
        actual = response['display']
        expected = '2'
        self.assertEqual(expected, actual)

    def test_sending_second_digit(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        actual = response['display']
        expected = '25'
        self.assertEqual(expected, actual)

    def test_sending_plus(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('+', response)
        actual = response['display']
        expected = '25'
        self.assertEqual(expected, actual)

    def test_sending_operator_after_operator(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('+', response)
        response = self.sendRequest('-', response)
        response = self.sendRequest(5,response)
        response = self.sendRequest('=',response)
        actual = response['display']
        expected = '20'
        self.assertEqual(expected, actual)

    def test_sending_minus(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('-', response)
        actual = response['display']
        expected = '25'
        self.assertEqual(expected, actual)

    def test_sending_division(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('/', response)
        actual = response['display']
        expected = '25'
        self.assertEqual(expected, actual)

    def test_sending_mult(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('*', response)
        actual = response['display']
        expected = '25'
        self.assertEqual(expected, actual)

    def test_sending_second_num(self):
        response = self.sendRequest(2)
        response = self.sendRequest(5,response)
        response = self.sendRequest('+', response)
        response = self.sendRequest(5,response)
        actual = response['display']
        expected = '5'
        self.assertEqual(expected, actual)

    def test_sending_equals(self):
        response = self.sendRequest(5)
        response = self.sendRequest('+',response)
        response = self.sendRequest(6, response)
        response = self.sendRequest('=', response)
        actual = response['display']
        expected = '11'
        self.assertEqual(expected, actual)

    def test_sending_equals_twice(self):
        response = self.sendRequest(5)
        response = self.sendRequest('+',response)
        response = self.sendRequest(6, response)
        response = self.sendRequest('=', response)
        response = self.sendRequest('=', response)
        actual = response['display']
        expected = '11'
        self.assertEqual(expected, actual)

    def test_sending_operator_after_equals(self):
        response = self.sendRequest(5)
        response = self.sendRequest('+',response)
        response = self.sendRequest(6, response)
        response = self.sendRequest('=', response)
        response = self.sendRequest('+',response)
        response = self.sendRequest(4, response)
        response = self.sendRequest('=', response)
        actual = response['display']
        expected = '15'
        self.assertEqual(expected, actual)

    def test_sending_number_after_operation(self):
        response = self.sendRequest(5)
        response = self.sendRequest('+', response)
        response = self.sendRequest(6, response)
        response = self.sendRequest('=', response)
        response = self.sendRequest(4, response)
        actual = response['display']
        expected = '4'
        self.assertEqual(expected, actual)

    def test_sending_operator_after_operation(self):
        response = self.sendRequest(3)
        response = self.sendRequest('*', response)
        response = self.sendRequest(3, response)
        response = self.sendRequest('=', response)
        response = self.sendRequest(4, response)
        response = self.sendRequest('*', response)
        response = self.sendRequest(2, response)
        actual = response['display']
        expected = '2'
        self.assertEqual(expected, actual)