from app.response import ResponseFactory
from app.routes import routes


class RoutingProvider:

    def __init__(self):
        self.routes = routes
        self.response = ResponseFactory()

    def router_evaluate(self, **kwargs):
        dynamic_argument = kwargs['path'].split('/')[-1]
        dynamic_path = kwargs['path'].replace(dynamic_argument, '{var}')

        body = kwargs['body']

        route = next((route for route in self.routes if route['path'] == kwargs['path']), None)
        d_route = next((d_route for d_route in self.routes if d_route['path'] == dynamic_path), None)

        if d_route and d_route['method'] == kwargs['method']:
            action = d_route['action'](argument=dynamic_argument, body=body)
            return self.response.ok_response(action)

        elif route and route['method'] == kwargs['method']:

            if route['action'] is not None:
                result = route['action'](body=body)
                return result
            else:
                return self.response.ok_response('OK')

        elif route and route['method'] != kwargs['method'] or d_route and d_route['method'] != kwargs['method']:
            if route is None:
                return self.response.not_allowed_response(d_route['method'])
            else:
                return self.response.not_allowed_response(route['method'])

        elif not d_route and not route:
            return self.response.not_found_response()
