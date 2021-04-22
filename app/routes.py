from app.greet import Greet

routes = [
    {'path': '/hello', 'action': Greet},
    {'path': '/hello/{var}', 'action': Greet},
    {'path': '/', 'action': Greet},
    {'path': '/favicon.ico', 'action': None}
]


