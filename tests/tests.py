from app.routes import routes
from app.greet import Greet
import urllib.parse as url
from app.router import routingService



rs = routingService()

path = 'http://localhost:8051/hello/Pablo'
result = rs.routerEval(path)
print(result)

