'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

from sqlalchemy.sql import func

def custom_query(database_class , session):
    '''
    This function finds the students who have grades 1.0 in atleast 3 courses.

    params : database_class : The class which defines the table
             session        : The session created for the connecting to the database

    return : query.all()    : The result of the query
    '''

    query = session.query(func.count(database_class.courses),database_class.name).filter_by(grade = 1.0).group_by(database_class.name).having(func.count(database_class.courses)>= 3.0)

    return query.all()
