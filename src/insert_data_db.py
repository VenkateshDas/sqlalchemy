'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

import csv
from schema import Task

def write_data_to_database(file_path,session):
    '''
    This function parses the dataset and inserts the data to the database connected.
    The file is parsed and read line by line to reduce the usage of the RAM during the whole process.

    params : file_path : The path to the CSV dataset
            session   : The session created for the connecting to the database

    return : lines : The total number of lines written in the dataset

    '''

    lines = 0
    object = []
    file = open(file_path,'r')
    numline = len(file.readlines())

    with open(file_path,'r') as f :

        reader = csv.reader(f, delimiter=',')
        next(reader) #skipping the header
        print("CSV File parsed")
        for row in reader:
            try:

                lines += 1
                # appending the table objects to the list
                object.append(Task(
                            name = row[0],
                            grade = row[1],
                            courses = row[2]
                            ))

                # For lists with length 1000
                if lines % 1000 == 0 :

                    session.bulk_save_objects(object) #insertion to database in bulk
                    session.commit()
                    print("Number of lines added : {}".format(lines))

                    object = []

                # For lists less than 1000 records
                elif lines == numline-1:
                    session.bulk_save_objects(object) #insertion to databse in bulk
                    session.commit()
                    print("Data Added")
                    break

            except Exception as e:
                 print("Unexpected error occured at line {} . Please look into the issue to make sure the program is running".format(lines))
                 print("The error occured : {}".format(e))
    return lines
