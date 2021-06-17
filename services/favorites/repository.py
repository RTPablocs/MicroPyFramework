from app.response import ResponseFactory
from services.database.controller import Db
from services.favorites.model import Like
from services.products.model import Products

db = Db()
resp = ResponseFactory()


def set_like(body):
    product_id = body['product_id']
    user_id = body['user_id']
    like = Like(product_id, user_id)
    is_like_set = db.session.query(Like).filter(Like.user_uid == user_id, Like.product_id == product_id).count()
    if is_like_set == 0:
        db.session.add(like)
        db.session.commit()
        return resp.ok_response('Like OK')
    else:
        return resp.forbidden_response()


def get_likes_from_user(**kwargs):
    user_id = kwargs['argument']
    likes_form_db = db.session.query(Like.product_id).filter(Like.user_uid == user_id).all()
    normalized_likes = [like_id for like in likes_form_db for like_id in like]
    products = db.session.query(Products).filter(Products.product_uid.in_(normalized_likes)).all()
    result = [product.serialize() for product in products]
    return resp.ok_response(result)


def delete_like(body):
    product_id = body['product_id']
    user_id = body['user_id']
    like = Like(product_id, user_id)
    db.session.delete(like)
    db.session.commit()
    return resp.ok_response('Like OK')
