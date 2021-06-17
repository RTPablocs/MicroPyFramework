from sqlalchemy import Column, String, ForeignKey
from services.database.controller import Db

db = Db()


class Like(db.base):
    __tablename__ = 'likes'
    product_id = Column(String , primary_key=True)
    user_uid = Column(String, primary_key=True)

    def __init__(self, product_id, user_id, ):
        self.product_id = product_id
        self.user_uid = user_id

    def serialize(self):
        return {
            'product_id': self.product_id,
            'user_id': self.user_uid,
        }

