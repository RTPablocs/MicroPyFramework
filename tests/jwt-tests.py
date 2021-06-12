from os import environ

import jwt
from dotenv import load_dotenv


class Authentication:

    def __init__(self):
        self.secret = environ['JWT_SECRET']
        self.algorithm = environ['JWT_ALGORITHM']

    def encode_jwt(self, data):
        token = jwt.encode(data, self.secret, algorithm=self.algorithm)
        return token

    def decode_jwt(self, token):
        data = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        return data


if __name__ == '__main__':
    load_dotenv('.env')

    payload = {'username': 'PAblocs', 'password': 'DSTD'}
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlBBYmxvY3MiLCJwXXNzd29yZCI6IkRTVEQifQ.2KUg8Sn9yuWDqzHwfGiV3AEjbHHIDYKwPxQvnGakZ6c'
    a = Authentication()
    #print(a.encode_jwt(payload))

    try:
        token_result = a.decode_jwt(token)
        print(token_result)

    except jwt.exceptions.InvalidSignatureError:
        print('Signature verification failed')
