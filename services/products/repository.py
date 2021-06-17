from uuid import uuid4

from app.response import ResponseFactory
from services.database.controller import Db
from services.products.model import Products

db = Db()
resp = ResponseFactory()


def get_all_products():
    products_list = [product.serialize() for product in db.session.query(Products).all()]
    return resp.ok_response(products_list)


def get_product_by_id(**kwargs):
    product = db.session.query(Products).get(kwargs['argument'])
    db.session.query(Products).filter_by(product_uid=kwargs['argument']).update(
        {'product_views': Products.product_views + 1})
    db.session.commit()
    return resp.ok_response(product.serialize())


def get_products_by_owner(**kwargs):
    products = db.session.query(Products).filter(Products.product_owner == kwargs['argument']).all()
    return resp.ok_response([product.serialize() for product in products])


def insert_product(body):
    product = Products(str(uuid4()), body['product_title'], body['product_desc'], body['product_brand'],
                       body['product_model'], body['product_category'], body['product_price'], body['product_miles'], 0,
                       body['product_owner'])
    db.session.add(product)
    db.session.commit()
    return resp.ok_response('Product OK')


def update_product(body):
    db.session.query(Products).filter(Products.product_uid == body['product_uid']).update(body)
    db.session.commit()
    product = db.session.query(Products).filter(Products.product_uid == body['product_uid']).first()
    return resp.ok_response(product.serialize())


def delete_product(body):
    product = Products(body['product_uid'], body['product_title'], body['product_desc'], body['product_brand'],
                       body['product_model'], body['product_category'], body['product_price'], body['product_miles'], 0,
                       body['product_owner'])
    db.session.delete(product)
    db.session.commit()
    return resp.ok_response('Product delete OK')
