class Car:

    def __init__(self,brand_id, brand_name, title, desc, mileage, price):
        self.brand_id = int
        self.brand_name = str
        self.title = str
        self.desc = str
        self.mileage = float
        self.price = float

    def return_as_dict(self):
        return self.__dict__
