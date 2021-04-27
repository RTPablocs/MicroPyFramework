import urllib.parse as url
from app.routes import routes


class RoutingProvider:

    def __init__(self):
        self.routes = routes

    def dynamic_evaluation(self, path, method):
        for r in self.routes:

            if '{var}' in r['path'] and path[-1] != '/':

                eval_path = url.urlparse(path).path.split('/')
                eval_path[-1] = '{var}'
                converted_path = '/'.join(eval_path)

                if converted_path == r['path'] and method == r['method']:
                    dynamic_argument = url.urlparse(path).path.split('/')[-1]
                    return {'path': converted_path, 'realPath': path, 'dynamic': True, 'dynamicArgument': dynamic_argument}

            elif r['path'] == path and method == r['method']:
                return {'path': path, 'dynamic': False}

    def router_evaluate(self, route, method):

        result_dict = self.dynamic_evaluation(route, method)

        for r in self.routes:
            if result_dict and result_dict['dynamic'] is True:
                action_result = r['action'](result_dict['dynamicArgument'])
                return {'code': '200 OK', 'actionResult': action_result}

            elif result_dict and result_dict['dynamic'] is False:
                action_result = r['action']()
                return {'code': '200 OK', 'actionResult': action_result}

            else:
                return {'code': '404 ERROR', 'actionResult': 'Path Not found'}
