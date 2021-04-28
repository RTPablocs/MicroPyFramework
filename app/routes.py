from app.greet import Greet

routes = [
    {'path': '/hello', 'method': 'GET', 'action': Greet},
    {'path': '/hello/{var}', 'method': 'POST', 'action': Greet},
    {'path': '/', 'method': 'GET', 'action': Greet},
    {'path': '/favicon.ico', 'method': 'GET', 'action': None}
]
