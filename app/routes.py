from services.favorites.repository import *
from services.products.repository import *
from services.users.repository import *

routes = [
    {'path': '/', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/favicon.ico', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/products', 'method': 'GET', 'action': get_all_products, 'requires_body': False},
    {'path': '/product/{var}', 'method': 'GET', 'action': get_product_by_id, 'requires_body': False},
    {'path': '/update/product', 'method': 'POST', 'action': update_product, 'requires_body': True},
    {'path': '/insert/product', 'method': 'POST', 'action': insert_product, 'requires_body': True},
    {'path': '/delete/product', 'method': 'POST', 'action': delete_product, 'requires_body': True},
    {'path': '/user/{var}', 'method': 'GET', 'action': get_user_info, 'requires_body': False},
    {'path': '/user/products/{var}', 'method': 'GET', 'action': get_products_by_owner, 'requires_body': False},
    {'path': '/verify/{var}', 'method': 'GET', 'action': verify_user, 'requires_body': False},
    {'path': '/login', 'method': 'POST', 'action': login_user, 'requires_body': True},
    {'path': '/register', 'method': 'POST', 'action': register_user, 'requires_body': True},
    {'path': '/register/social', 'method': 'POST', 'action': register_user, 'requires_body': True},
    {'path': '/favorite', 'method': 'POST', 'action': set_like, 'requires_body': True},
    {'path': '/favorites/user/{var}', 'method': 'GET', 'action': get_likes_from_user, 'requires_body': False}
]
