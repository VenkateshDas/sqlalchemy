from sqlalchemy import Column, Integer, String, Date, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base

#To setup the class for the creation of table  (Look into the reason for creating this super class)
Base = declarative_base()

#variable for the auto increment primary key in the table
TABLE_ID = Sequence('table_id_seq', start= 1 )


#Creating a class for the database schema - table "tasks" . The attributed can be accessed inside the python script by
#initialising the object for the class.
class Task(Base):
    __tablename__ = 'task_table'
    id = Column(Integer, TABLE_ID , primary_key=True , server_default=TABLE_ID.next_value() )
    name = Column(String)
    grade = Column(Float)
    courses = Column(String)

    def __repr__(self):
        return "<Task(id = '{}',name='{}', grade='{}', courses={})>"\
                .format(self.id, self.name, self.grade, self.courses)
