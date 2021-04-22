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
                convertedPath = '/'.join(evalPath)
                
                if cPath == r['path']: 
                    dynamicArgument = url.urlparse(p).path.split('/')[-1]
                    return {'path': convertedPath, 'realPath': p, 'dynamic': True, 'dynamicArgument': dynamicArgument}

            elif r['path'] == p:
                return  {'path': p, 'dynamic': False}
                    

    def routerEval(self, route):

        resultDict = self.dynamicEval(route)
        
        
        for r in self.routes:
            if resultDict and resultDict['dynamic'] == True: 
                actionResult = r['action'](resultDict['dynamicArgument'])
                return {'code': '200 OK', 'actionResult': resultDict}
            
            elif resultDict and resultDict['dynamic'] == False:
                actionResult = r['action']()
                return{'code': '200 OK', 'actionResult': actionResult}

            elif resultDict and resultDict['path'] not in r['path'] : 
                return {'code': '404 ERROR', 'actionResult': 'Path Not found'}
            