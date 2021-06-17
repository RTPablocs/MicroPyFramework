from sqlalchemy import Column, Integer, String, ForeignKey

from services.database.controller import Db

db = Db()


class Products(db.base):
    __tablename__ = 'products'

    product_uid = Column(String, primary_key=True)
    product_title = Column(String)
    product_desc = Column(String)
    product_brand = Column(String)
    product_model = Column(String)
    product_category = Column(String)
    product_price = Column(Integer)
    product_miles = Column(Integer)
    product_views = Column(Integer)
    product_owner = Column(String)

    def __init__(self, product_uid, product_title, product_desc, product_brand, product_model, product_category,
                 product_price, product_miles, product_views, product_owner):
        self.product_uid = product_uid
        self.product_title = product_title
        self.product_desc = product_desc
        self.product_brand = product_brand
        self.product_model = product_model
        self.product_category = product_category
        self.product_price = product_price
        self.product_miles = product_miles
        self.product_views = product_views
        self.product_owner = product_owner

    def serialize(self):
        return {
            'product_uid': self.product_uid,
            'product_title': self.product_title,
            'product_desc': self.product_desc,
            'product_brand': self.product_brand,
            'product_model': self.product_model,
            'product_category': self.product_category,
            'product_price': self.product_price,
            'product_miles': self.product_miles,
            'product_views': self.product_views,
            'product_owner': self.product_owner
        }
