# !/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from request_to_executor_mapper import *


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        # Send message back to client
        message = {"message": "Hello World"}
        message_as_json = json.dumps(message)
        # Write content as utf-8 data
        self.wfile.write(bytes(message_as_json, "utf8"))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length)
        args = json.load(request_body)
        executor = RequestToExecutorMapper.get_executor(self.path)
        response = executor.execute(args)
        self.respond(self,response)

    def respond(self, response):
        #response={'status':'all_ok','body':{}}
        #dic={'all_ok':200}
        self.send_response(response['status'])
        # self.send_header('Content-type', 'teext/json')
        # self.end_headers()
        # message_as_json = json.dumps(response['body'])
        # # Write content as utf-8 data
        # self.wfile.write(bytes(message_as_json, "utf8"))


def run():
    config = json.load(open('config.json'))
    port = config['port']
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
