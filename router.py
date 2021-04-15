from routes import routes

class router:

    def __init__(self):
        self.routes = routes
    
    def routerEval(self, route):

        for r in self.routes:
            if r['path'] == route: 
                actionResult = r['action']()
                responseByRoute = {'code': '200 OK', 'actionResult': actionResult}
            else:
                responseByRoute = {'code': '404 ERROR', 'actionResult': 'Path not found'}
        return responseByRoute
        