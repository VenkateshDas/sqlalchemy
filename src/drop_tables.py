from db import setup_db_connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
from schema import Task, Base

def drop_tables(engine):
    Base.metadata.drop_all(engine)

db_name = input("Enter the name of the database to be connected : ")

engine = setup_db_connection('tasks')

drop_tables(engine)

inspector = inspect(engine)
tables = inspector.get_table_names()

if tables == []:
    print("Tables got deleted . No tables currently ")

else:
    print(tables)
    print("Error the tables did not get deleted")
