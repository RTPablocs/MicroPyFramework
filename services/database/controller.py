from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Db:
    def __init__(self):
        self.engine = create_engine('sqlite:///carapp.sqlite3?check_same_thread=False')
        self.session_conn = sessionmaker(bind=self.engine)
        self.session = self.session_conn()
        self.base = declarative_base()
