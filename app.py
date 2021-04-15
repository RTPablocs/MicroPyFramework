from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults, application_uri
from banner import BannerSpawn

class App:

    def __init__(self):
        self.PORT = 8051
        self.HOST = 'localhost'
        self.motd = BannerSpawn()

    def baseServe(self, environ, start_response):

        status = '200 OK'
        headers = [('Content-Type', 'application/json; charset=utf-8')]
        body = 'AAA'
        start_response(status, headers)

        ret = [body.encode('utf-8')]

        return ret

    def run(self): 
        with make_server(self.HOST, self.PORT, self.responseFactory) as httpd:
            print(self.motd, '\n', 'Serving app on port:', self.PORT)
            httpd.serve_forever()
                