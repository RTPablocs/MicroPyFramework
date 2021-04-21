from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults, request_uri
from app.router import routingService
from app.parseURL import urlParse
from extensions.banner import bannerSpawn
import os

class app:

    def __init__(self):
        self.PORT = 8051
        self.HOST = 'localhost'
        self.motd = bannerSpawn()
        self.router = routingService()
        self.version = 'v0.1-rc2'

    def baseServe(self, environ, start_response):
        path = urlParse(str(request_uri(environ)))
        result = self.router.routerEval(path)
        status = result['code']
        headers = [('Content-Type', 'application/json; charset=utf-8')]
        
        start_response(status, headers)
        
        return [str(result).encode()]

    def run(self):
        with make_server(self.HOST, self.PORT, self.baseServe) as httpd:
            print(self.motd, '\n', 'Serving app on port:', self.PORT, '\n', self.version )
            httpd.serve_forever()
