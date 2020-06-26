'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

from sqlalchemy import Column, Integer, String, Date, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base

'''
To setup the class for the creation of table
'''
Base = declarative_base()

TABLE_ID = Sequence('table_id_seq', start= 1 )      #variable for the auto increment primary key in the table

class Task(Base):
    '''
    Creating a class for the database schema - table "task_table" .
    The attributes can be accessed inside the python script by
    initialising the object for the class.
    '''
    __tablename__ = 'task_table'
    id = Column(Integer, TABLE_ID , primary_key=True , server_default=TABLE_ID.next_value() )
    name = Column(String)
    grade = Column(Float)
    courses = Column(String)

    def __repr__(self):
        '''
        A format to visualise the result.
        '''
        return "<Task(id = '{}',name='{}', grade='{}', courses={})>"\
                .format(self.id, self.name, self.grade, self.courses)
