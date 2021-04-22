from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults, request_uri
from app.router import RoutingProvider
from extensions.utils import url_parse
from extensions.utils import banner_generate


class app:

    def __init__(self):
        self.PORT = 8051
        self.HOST = 'localhost'
        self.motd = banner_generate()
        self.router = RoutingProvider()
        self.version = 'v0.1-rc2'

    def app_server(self, environ, start_response):
        path = url_parse(str(request_uri(environ)))
        result = self.router.router_evaluate(path)
        status = result['code']
        headers = [('Content-Type', 'application/json; charset=utf-8')]

        start_response(status, headers)

        return [str(result).encode()]

    def run(self):
        with make_server(self.HOST, self.PORT, self.app_server) as httpd:
            print(self.motd, '\n', 'Serving app on port:', self.PORT, '\n', self.version)
            httpd.serve_forever()
