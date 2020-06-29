'''
__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"
'''

'''
This program is created to see the rows in the csv dataset
'''

import csv

def print_csv_rows(reader):
  """This function prints the rows in the reader object

  Args:
      reader ([Iterator object]): CVS reader object
  """
  for row in reader:
    print(row)

file = 'test_data_files/random_test_small.csv'

reader = csv.reader(open(file,'r'),delimiter=',')
print_csv_rows(reader)
