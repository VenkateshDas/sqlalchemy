import numpy as np
import pandas as pd
columns = ['name','grade','courses']
df = pd.DataFrame(columns = columns)

size = 1000000

names = ['Mike','Alex','Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Oliver','Sophia','Benjamin','Charlotte','Elijah','Mia','Lucas','Amelia','Mason','Harper','Logan']
df['name'] = np.random.choice(list(names), size)

grades = [1.0,2.0,3.0,4.0,5.0]
df['grade'] = np.random.choice(list(grades),size )

courses = ['Programming', 'Physics', 'Science', 'Chemistry', 'Biology', 'English', 'Maths', 'German']
df['courses'] = np.random.choice(list(courses), size)

df.head()

print(len(df))

f = open('random_test_small.csv', 'w')
df.to_csv( f , encoding='utf-8',index=False)
