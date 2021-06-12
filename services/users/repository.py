from app.auth import Authorization
from app.response import ResponseFactory
from services.database.controller import Db
from services.users.model import User
import uuid

auth = Authorization()
db = Db()
resp = ResponseFactory()


def get_user_info(**kwargs):
    userid = kwargs['argument']
    user_info = db.session.query(User).get(userid)
    if user_info is not None:
        return resp.ok_response(user_info.serialize())
    else:
        return resp.not_found_response()


def login_user(body):
    mail = body['email']
    db_response = db.session.query(User).filter_by(user_email=mail).all()

    if db_response:
        user_info = db_response[0].serialize()
        if user_info['user_password'] == body['password']:
            token = auth.encode_token(user_info)
            db.session.close()
            return resp.ok_response(token)
        else:
            return resp.forbidden_response()
    else:
        return resp.not_found_response()


def register_user(body):
    id = str(uuid.uuid4())
    mail = body['email']
    user_name = body['user']
    password = body['password']
    count = db.session.query(User).filter_by(user_email=mail).count()
    if count != 1:
        user = User(id, user_name, mail, password)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return resp.ok_response('User OK')
    else:
        return resp.forbidden_response()
