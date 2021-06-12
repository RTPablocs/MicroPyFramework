from services.products.repository import *
from services.users.repository import *

routes = [
    {'path': '/', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/favicon.ico', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/products', 'method': 'GET', 'action': get_all_products, 'requires_body': False},
    {'path': '/product/{var}', 'method': 'GET', 'action': get_product_by_id, 'requires_body': False},
    {'path': '/user/{var}', 'method': 'GET', 'action': get_user_info, 'requires_body': False},
    {'path': '/login', 'method': 'POST', 'action': login_user, 'requires_body': True},
    {'path': '/register', 'method': 'POST', 'action': register_user, 'requires_body': True}
]
