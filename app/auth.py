from os import environ
import jwt


class Authorization:
    def __init__(self):
        self.secret = environ.get('JWT_SECRET')
        self.algorithm = environ.get('JWT_ALGORITHM')

    def encode_token(self, data):
        token = jwt.encode(data, self.secret, algorithm=self.algorithm)
        return token

    def decode_token(self, token):
        data = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        return data
