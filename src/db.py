'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

from sqlalchemy import create_engine
from schema import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

def setup_db_connection(database_name):
    '''
    This function creates the connection to the PostgreSQL database.
    The database is created in advance with the PostgreSQL interface.

    params : database_name : The name of the database in the PostgreSQL Server
    return : engine        : The object that interacts with the database

    '''


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
    '''
    This function creates the session for the interaction with the database for the transactions.
    And it creates the table specified in the database schema (schema.py)

    params : engine : The object that interacts with the database.
    returns : session : The created session with the engine.
    '''
    Session = sessionmaker(bind=engine)
    session = Session()
    create_table(engine)
    return session

def create_table(engine):
    '''
    This function creates the table in the schema.

    params : engine : The object that interacts with the database.
    return : none
    '''
    Base.metadata.create_all(engine)
