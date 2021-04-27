from app.greet import Greet

routes = [
    {'path': '/hello', 'method': 'GET', 'action': Greet},
    {'path': '/hello/{var}', 'method': 'GET', 'action': Greet},
    {'path': '/', 'action': Greet},
    {'path': '/favicon.ico', 'action': None}
]
