import argparse
from schema import *
from db import setup_db_connection , create_session 
from insert_data_db import write_data_to_database
from query import custom_query
import time



def main():

    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('--h',help = 'Usage')
    parser.add_argument('--db_name', help='Database name to be connected')
    parser.add_argument('--csv_file_path', help = 'File path of the CSV dataset')

    args = parser.parse_args()

    if args.h == 'help':
        print("usage : main.py --db_name --csv_file_path")

    start_time = time.time()

    engine = setup_db_connection(args.db_name)

    print(" Connection Established with the Postgres Database ")

    session = create_session(engine)

    print(" New table is created ")

    num_lines = write_data_to_database(args.csv_file_path,session)

    print("Total number of lines added to Database : {}".format(num_lines))

    end_time = time.time() - start_time

    print("Total time to read and write the database : {} ".format(end_time))

    print("="*50)

    print(
    '''
    Custom Query : A function that queries the database for all students that got grade
    1.0 in at least 3 classes and prints all results (In the example file that would be
    Milana

    ''' )

    custom_query_result = custom_query(Task , session )
    print(custom_query_result)

    session.close()


if __name__ == "__main__":
    main()
