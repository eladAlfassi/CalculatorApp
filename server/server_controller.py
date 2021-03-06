# !/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import json
import os
#from request_to_executor_mapper import *
#from HttpResponseDict import *
from server.request_to_executor_mapper import *
from server.HttpResponseDict import *
import logging


# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        # Send message back to client
        message = {"display": "55"}
        message_as_json = json.dumps(message)
        # Write content as utf-8 data
        self.wfile.write(bytes(message_as_json, "utf8"))
        return

    def do_POST(self):
        #print("SERVER: in do post")
        content_length = int(self.headers['Content-Length'])
        request_body = self.rfile.read(content_length).decode('utf-8')
        logging.debug('\nCLIENT input:'+ request_body)
        args = json.loads(request_body)
        global req_to_map
        executor = req_to_map.get_executor(self.path)
        response = executor.execute(args)
        self.respond(response)

    def respond(self, response):
        logging.debug('\nSERVER: response dict is: '+str(response)+'\n')
        httpResponseDict = HttpResponseDict()
        self.send_response(httpResponseDict[response['status']])
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        message_as_json = json.dumps(response)
        # # Write content as utf-8 data
        self.wfile.write(bytes(message_as_json, "utf8"))



def run():
    import os
    sys.path.insert(0, '/app/server')
    #config = json.load(open('server/config.json'))
    #port=config['port']
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    port=5000
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print('running server on port {0}...'.format(str(port)))

    httpd.serve_forever()

if __name__ == "__main__":
    run()

req_to_map=RequestToExecutorMapper()
