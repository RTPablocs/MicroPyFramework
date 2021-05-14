import json
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'application/json; charset=utf-8')]

    start_response(status, headers)
    content_size = environ['CONTENT_LENGTH']
    if content_size != '':

        request_body = environ['wsgi.input'].read(int(content_size))
        request_json = json.loads(request_body)
        response_placeholder = {'code': '200 OK', 'response': request_json}

        response = json.dumps(response_placeholder).encode('utf-8')

        return [response]
    else:
        method = environ['REQUEST_METHOD']
        return [method.encode('utf-8')]


with make_server('', 8090, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
