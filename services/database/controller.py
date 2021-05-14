from os import environ
from mysql.connector import connect, Error


class DataBaseController:

    def __init__(self):
        self.user = environ['MYSQL_USER']
        self.host = environ['MYSQL_HOST']
        self.password = environ['MYSQL_PASSWD']
        self.database = environ['MYSQL_DB']

    def connector(self):
        try:
            with connect(host=self.host, user=self.user, password=self.password) as conn:
                return conn
        except Error as e:
            return e

    def insert_one(self, **kwargs):
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute()
