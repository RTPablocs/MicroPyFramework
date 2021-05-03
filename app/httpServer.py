from socketserver import ThreadingMixIn
from wsgiref.simple_server import make_server, WSGIServer
from wsgiref.util import request_uri

from app.router import RoutingProvider
from extensions.utils import banner_generate
from extensions.utils import url_parse


class MultiThreading(ThreadingMixIn, WSGIServer):
    daemon_threads = True


class App:

    def __init__(self):
        self.PORT = 8051
        self.HOST = 'localhost'
        self.motd = banner_generate()
        self.router = RoutingProvider()
        self.version = 'v0.1-rc3'

    def app_server(self, environ, start_response):
        path = url_parse(str(request_uri(environ)))
        method = environ['REQUEST_METHOD']
        result = self.router.router_evaluate(path, method)
        status = result['code']
        headers = [('Content-Type', 'application/json; charset=utf-8')]

        start_response(status, headers)

        return [str(result).encode()]

    def run(self):
        with make_server(self.HOST, self.PORT, self.app_server, MultiThreading) as httpd:
            print(self.motd, '\n', 'Serving app on port:', self.PORT, '\n', self.version)
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print('Shutting down, bye!')
                httpd.server_close()
