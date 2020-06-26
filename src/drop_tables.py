'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

from db import setup_db_connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
from schema import Task, Base

def drop_tables(engine):
    '''
    This function deletes all the table in the database.

    params : engine : The object that interacts with the database.
    return : none
    '''
    Base.metadata.drop_all(engine)

db_name = input("Enter the name of the database to be connected : ")    # name of the database

engine = setup_db_connection(db_name)                                   #connect to the database

drop_tables(engine)                                                     # a call to delete the dataset

inspector = inspect(engine)                                             # an object to inspect the database
tables = inspector.get_table_names()                                    # getting the names of the table in the database

if tables == []:
    print("Tables got deleted . No tables currently ")

else:
    print(tables)
    print("Error the tables did not get deleted")
