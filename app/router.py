import urllib.parse as url
from app.routes import routes


class RoutingProvider:

    def __init__(self):
        self.routes = routes

    def dynamic_evaluation(self, p):
        for r in self.routes:

            if '{var}' in r['path'] and p[-1] != '/':

                eval_path = url.urlparse(p).path.split('/')
                eval_path[-1] = '{var}'
                converted_path = '/'.join(eval_path)

                if converted_path == r['path']:
                    dynamic_argument = url.urlparse(p).path.split('/')[-1]
                    return {'path': converted_path, 'realPath': p, 'dynamic': True, 'dynamicArgument': dynamic_argument}

            elif r['path'] == p:
                return {'path': p, 'dynamic': False}

    def router_evaluate(self, route):

        result_dict = self.dynamic_evaluation(route)

        for r in self.routes:
            if result_dict and result_dict['dynamic'] is True:
                action_result = r['action'](result_dict['dynamicArgument'])
                return {'code': '200 OK', 'actionResult': action_result}

            elif result_dict and result_dict['dynamic'] is False:
                action_result = r['action']()
                return {'code': '200 OK', 'actionResult': action_result}

            else:
                return {'code': '404 ERROR', 'actionResult': 'Path Not found'}
