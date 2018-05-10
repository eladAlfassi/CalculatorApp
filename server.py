# !/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import HttpResponseDict
from request_to_executor_mapper import *


# HTTPRequestHandler class
class CalculatorServer(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        args = json.load(request_body)
        executor = RequestToExecutorMapper.get_executor(self.path)
        response = executor.execute(args)
        self.respond(self,response)

    def respond(self, response):
        httpResponseDict = HttpResponseDict()
        self.send_response(httpResponseDict[response['header']])
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        message_as_json = json.dumps(response['body'])
        # # Write content as utf-8 data
        self.wfile.write(bytes(message_as_json, "utf8"))


def run():
    config = json.load(open('config.json'))
    port = config['port']
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, CalculatorServer)
    print('running server...')
    httpd.serve_forever()


run()
