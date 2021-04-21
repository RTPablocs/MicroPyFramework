import urllib.parse as url
from app.routes import routes

class routingService:

    def __init__(self):
        self.routes = routes
    
    def dynamicEval(self, p):
        for r in self.routes:

            if '{var}' in r['path'] and p[-1] != '/':

                evalPath = url.urlparse(p).path.split('/')
                evalPath[-1] = '{var}'
                cPath = '/'.join(evalPath)
                
                if cPath == r['path']: 
                    dynamic = url.urlparse(p).path.split('/')[-1]
                    return {'path': cPath, 'realPath': p, 'dynamic': True, 'dynamicArgument': dynamic}

            elif r['path'] == p:
                return  {'path': p, 'dynamic': False}
                    

    def routerEval(self, route):

        rDict = self.dynamicEval(route)
        
        for r in self.routes:
            if r['path'] == rDict['path'] and rDict['dynamic'] == True  : 
                actionResult = r['action'](rDict['dynamicArgument'])
                return {'code': '200 OK', 'actionResult': actionResult}
            
            elif r['path'] == rDict['path'] and rDict['dynamic'] == False:
                actionResult = r['action']()
                return{'code': '200 OK', 'actionResult': actionResult}

            elif rDict['path'] not in r['path'] : 
                return {'code': '404 ERROR', 'actionResult': 'Path Not found'}
            