class ResponseFactory:
    def __init__(self):
        self.ok_code = '200 OK'
        self.svr_error_code = '500 ERR0R'
        self.clnt_error_code = '400 ERROR'
        self.not_found_code = '404 ERROR'
        self.forbidden_code = '403 ERROR'
        self.not_allowed_code = '405 ERROR'

    def ok_response(self, action):
        response = {'code': self.ok_code, 'result': action}
        return response

    def not_found_response(self):
        response = {'code': self.not_found_code, 'description': 'Path not found on this server'}
        return response

    def forbidden_response(self):
        response = {'code': self.forbidden_code, 'description': 'Forbidden access to this path'}
        return response

    def client_error_response(self):
        response = {'code': self.clnt_error_code, 'description': 'Bad request, retry'}
        return response

    def srv_error_response(self, description):
        response = {'code': self.svr_error_code, 'description': description}
        return response

    def not_allowed_response(self, method):
        response = {'code': self.not_allowed_code,
                    'description': 'Method not allowed, use {method} instead'.format(method=method)}
        return response


def custom_response(code, description):
    response = {'code': code, 'description': description}
    return response
