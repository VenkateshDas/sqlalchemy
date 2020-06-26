from sqlalchemy import create_engine
from schema import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

def setup_db_connection(database_name):

    # database_name = input("Enter the database name to be connected")

    db_url = {'drivername': 'postgres+psycopg2',
          'username': 'postgres',
          'password': '39126',
          'host': 'localhost',
          'port': 5432,
          'database' : database_name }

    engine = create_engine(URL(**db_url))
    return engine

#create session
def create_session(engine):
    Session = sessionmaker(bind=engine)
    s = Session()
    create_table(engine)
    return s

def create_table(engine):
    Base.metadata.create_all(engine)
