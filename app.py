from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults, request_uri
from banner import bannerSpawn
from router import router
import os

class app:

    def __init__(self):
        self.PORT = 8051
        self.HOST = 'localhost'
        self.motd = bannerSpawn()
        self.router = router()

    def baseServe(self, environ, start_response):
        path = str(request_uri(environ)).split('/')[-1]
        
        result = self.router.routerEval(path)
        status = result['code']
        headers = [('Content-Type', 'application/json; charset=utf-8')]
        
        start_response(status, headers)
        
        ret = result['actionResult']
        
        return [ret.encode()]

    def run(self):
        with make_server(self.HOST, self.PORT, self.baseServe) as httpd:
            print(self.motd, '\n', 'Serving app on port:', self.PORT)
            httpd.serve_forever()
