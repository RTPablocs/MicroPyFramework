import urllib.parse as url
from app.routes import routes
from app.response import ResponseFactory


class RoutingProvider:

    def __init__(self):
        self.routes = routes
        self.response = ResponseFactory()

    def dynamic_evaluation(self, path, method):
        for r in self.routes:

            if '{var}' in r['path'] and path[-1] != '/':

                eval_path = url.urlparse(path).path.split('/')
                eval_path[-1] = '{var}'
                converted_path = '/'.join(eval_path)

                if converted_path == r['path'] and method == r['method']:
                    dynamic_arg = url.urlparse(path).path.split('/')[-1]
                    return {'path': converted_path, 'realPath': path, 'dynamic': True, 'dynamicArgument': dynamic_arg}

            elif r['path'] == path and method == r['method']:
                return {'path': path, 'dynamic': False}

    def router_evaluate(self, route, method):

        result_dict = self.dynamic_evaluation(route, method)

        for r in self.routes:
            if result_dict and result_dict['dynamic'] is True:
                action_result = r['action'](result_dict['dynamicArgument'])
                return self.response.ok_response(action_result)

            elif result_dict and result_dict['dynamic'] is False:
                action_result = r['action']()
                return self.response.ok_response(action_result)

            else:
                return self.response.not_found_response()
