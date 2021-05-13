from os import environ


class Authorization:
    def __init__(self):
        self.token = environ['JWT_SECRET']
    def encode_token(self, token):
        pass

