from services.products.repository import *

routes = [
    {'path': '/', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/favicon.ico', 'method': 'GET', 'action': None, 'requires_body': False},
    {'path': '/products', 'method': 'GET', 'action': get_all_products, 'requires_body': False},
    {'path': '/product/{var}', 'method': 'GET', 'action': get_product_by_id, 'requires_body': False}
]
