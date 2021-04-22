from app.routes import routes
from app.greet import Greet
import urllib.parse as url
from app.router import RoutingProvider

rs = RoutingProvider()

path = 'http://localhost:8051/df'
result = rs.router_evaluate(path)
print(result)
