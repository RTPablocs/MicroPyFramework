from app.response import ResponseFactory
from services.database.controller import Db
from services.products.model import Products

db = Db()
resp = ResponseFactory()


def get_all_products():
    products_list = []
    for product in db.session.query(Products).all():
        products_list.append(product.serialize())
    return resp.ok_response(products_list)


def get_product_by_id(**kwargs):
    product = db.session.query(Products).get(kwargs['argument'])
    db.session.query(Products).filter_by(product_uid=kwargs['argument']).update(
        {'product_views': Products.product_views + 1})
    db.session.commit()
    return resp.ok_response(product.serialize())
