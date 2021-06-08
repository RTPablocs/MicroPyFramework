from services.database.controller import Db
from services.users.model import User

db = Db()


def get_user_info(user_id):
    user_info = db.session.query(User).get(user_id)
    return user_info.serialize()

# def insert_user():
