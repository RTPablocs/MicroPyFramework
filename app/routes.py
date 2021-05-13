from app.greet import Greet
from app.farewell import Farewell
from app.body import body_serve
routes = [
    {'path': '/hello', 'method': 'GET', 'action': Farewell},
    {'path': '/hello/{var}', 'method': 'POST', 'action': Greet},
    {'path': '/', 'method': 'GET', 'action': Farewell},
    {'path': '/favicon.ico', 'method': 'GET', 'action': None},
    {'path': '/body', 'method': 'POST', 'action': body_serve}
]
