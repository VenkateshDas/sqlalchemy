'''

__author__    = "Venkatesh Murugadas"
__date__      = "26.06.2020"
__version__   = "1.0"
__maintainer__= "Venkatesh Murugadas"
__email__     = "venkatesh.murugadas@st.ovgu.de"
__status__    = "Draft"

'''

import numpy as np
import pandas as pd

columns = ['name','grade','courses']    #create columns
df = pd.DataFrame(columns = columns)

size = 1000000      # The number of lines in the dataset

names = ['Mike','Alex','Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Oliver','Sophia','Benjamin','Charlotte','Elijah','Mia','Lucas','Amelia','Mason','Harper','Logan']
df['name'] = np.random.choice(list(names), size) # Filling the names randomly

grades = [1.0,2.0,3.0,4.0,5.0]
df['grade'] = np.random.choice(list(grades),size ) # Filling the grades randomly

courses = ['Programming', 'Physics', 'Science', 'Chemistry', 'Biology', 'English', 'Maths', 'German']
df['courses'] = np.random.choice(list(courses), size) # Filling the courses randomly

f = open('random_test_small.csv', 'w')
df.to_csv( f , encoding='utf-8',index=False) #index is False to avoid the id column from the Dataframe. 
