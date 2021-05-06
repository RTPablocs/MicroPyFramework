from app.response import ResponseFactory
from app.routes import routes


class RoutingProvider:

    def __init__(self):
        self.routes = routes
        self.response = ResponseFactory()
        self.json_headers = [('Content-Type', 'application/json')]

    def router_evaluate(self, path, method):
        dynamic_argument = path.split('/')[-1]
        dynamic_path = path.replace(dynamic_argument, '{var}')

        route = next((route for route in self.routes if route['path'] == path), None)
        d_route = next((d_route for d_route in self.routes if d_route['path'] == dynamic_path), None)

        if d_route and d_route['method'] == method:
            action = d_route['action'](dynamic_argument)
            return self.response.ok_response(action)

        elif route and route['method'] == method:

            if route['action'] is not None:
                action = route['action']()
                return self.response.ok_response(action)
            else:
                return self.response.ok_response('OK')

        elif route and route['method'] != method or d_route and d_route['method'] != method:
            if route is None:
                return self.response.not_allowed_response(d_route['method'])
            else:
                return self.response.not_allowed_response(route['method'])

        elif not d_route and not route:
            return self.response.not_found_response()
