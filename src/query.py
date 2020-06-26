
from sqlalchemy.sql import func

def custom_query(database_class , session):

    query = session.query(func.count(database_class.courses),database_class.name).filter_by(grade = 1.0).group_by(database_class.name).having(func.count(database_class.courses)>= 3.0)

    return query.all()
