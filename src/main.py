'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

import argparse
from schema import *
from db import setup_db_connection , create_session
from insert_data_db import write_data_to_database
from query import custom_query
import time



def main():
    '''
    This is the main function which calls the necessary functions to solve the provided task.

    This function takes 3 command line arguments.

    --h             help usage of the code
    --db_name       the name of the database
    --csv_file_path the path of the csv used for processing

    params : none
    return : none

    '''

    # parser arguments
    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('--h',help = 'Usage')
    parser.add_argument('--db_name', help='Database name to be connected')
    parser.add_argument('--csv_file_path', help = 'File path of the CSV dataset')

    args = parser.parse_args()

    #log time
    start_time = time.time()

    engine = setup_db_connection(args.db_name)                      #initiating the connection

    print(" Connection Established with the Postgres Database ")

    session = create_session(engine)                                #creating tables and session

    num_lines = write_data_to_database(args.csv_file_path,session)  #parse and write data to Database

    print("Total number of lines added to Database : {}".format(num_lines))

    end_time = time.time() - start_time

    print("Total time to read and write the database : {} ".format(end_time))

    print("="*50)

    print(
    '''
    Custom Query : A function that queries the database for all students that got grade
    1.0 in at least 3 classes and prints all results (In the example file that would be
    Milana

    SQL statement :

    SELECT Count(courses) , name
    FROM task_table
    WHERE grade = 1.0 GROUP BY name HAVING Count(courses) >= 3.0

    ''' )

    custom_query_result = custom_query(Task , session )             # SQLAlchemy ORM based query call
    print(custom_query_result)

    session.close()


if __name__ == "__main__":
    main()
