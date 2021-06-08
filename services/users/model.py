from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from services.database.controller import Db

db = Db()


class User(db.base):
    __tablename__ = 'users'
    user_uid = Column(String, primary_key=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    product = relationship('Products')
    likes = relationship('Likes')

    def __init__(self, user_uid, user_name, user_email, user_password):
        self.user_uid = user_uid
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def serialize(self):
        return {
            'user_uid': self.user_uid,
            'user_name': self.user_name,
            'user_mail': self.user_email,
            'user_password': self.user_password
        }
