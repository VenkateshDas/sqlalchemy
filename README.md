# SQLAlchemy 
This repository is created to showcase the task provided by Martin Glauer. 

## **Tasks:**

	1. Create a database schema using SQLAlchemy  that can store the data provided in the file. 
	2. A function that reads the file and stores the data in the tables from 1. Hint: This function should be abe to handle datasets that are large (several GB) without flooding my RAM ;)
	3. A function that queries the database for all students that got grade  1.0 in at least 3 classes and prints all results (In the example file that  would be  Milana)

## Requirements :

### Packages

 - To run the above code PostgreSQL and psycopg2 are required to create a database. 
- SQLAlchemy 
- Python 3

### Files
- A CSV file that contains the data contains the data that has to be added to the database on which the query is carried out. 

### Usage : 

usage: main.py  -h --db_name DB_NAME --csv_file_path CSV_FILE_PATH

SQLAlchemy Task code

optional arguments:
  -h, --help            show this help message and exit
  --db_name DB_NAME -->"Database name to be connected"
  --csv_file_path CSV_FILE_PATH  --> "File path of the CSV dataset"

DB_NAME is the database that has been created in the Postgres server to which the user wants to connect for further processing. 

## Procedure

### Database
To solve the tasks I created two solutions. 
1. Using sqlite to process small datasets that can be run without creating a server. I wanted to create an initial working prototype so I chose to develop in the Colab notebook environment. 
2. The second solution was to create a server locally using PostgreSQL . PostgreSQL proivdes a dashboard to manage the databases, creates the transactions on persistent memory and clears the RAM.  

### Parsing 
The parsing of the CSV dataset is done using csv reader module instead of using Pandas. Due to the objective that there is no manipulation to be done on the dataset and this also eleminates the overhead caused by Pandas. 

### Inserting data to Database 
- The data is read one by one from the reader instance from the csv reader. This will not hold up a lot of RAM during the runtime. 
- Using the ORM functionality in SQLAlchemy of bulk insert, the addition of data to databse can be optimised by sending bulk data at a point in time. And then commited to the database. 
- This can be carried out for computational efficency. 

### Query 
- session.query(func.count(database_class.courses),database_class.name).filter_by(grade=1.0).group_by(database_class.name).having(func.count(database_class.courses)>= 3.0) 
