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
- A database in the PostgreSQL server

### Usage : 

    python main.py  -h --db_name DB_NAME --csv_file_path CSV_FILE_PATH

#### Example : 

    python main.py --db_name tasks --csv_file_path test_data_files/task.csv

SQLAlchemy Task code

    optional arguments:
      -h, --help            show this help message and exit
      --db_name DB_NAME "Database name to be connected"
      --csv_file_path CSV_FILE_PATH "File path of the CSV dataset"

DB_NAME is the database that has been created in the Postgres server to which the user wants to connect for further processing. 

## Procedure

### Intro 
An image that explains the reason for the usage of the SQLAlchemy. It creates a connection  between the program and the database for interaction. The Object Relational Mapping functionality helps to code in python without the hassle as in raw SQL and be more pythonic. 

![sqlalchemy](test_images/session.png)

### Database
To solve the tasks I created two solutions. 
1. Using sqlite to process small datasets that can be run without creating a server. I wanted to create an initial working prototype so I chose to develop in the Colab notebook environment. 
2. The second solution was to create a server locally using PostgreSQL . PostgreSQL proivdes a dashboard to manage the databases, creates the transactions on persistent memory and clears the RAM.  

The SQLite implementation is provided in the colab notebook version. The PostgreSQL version is provided in the src folder. The usage of this folder is provided above. 

### Parsing 
The parsing of the CSV dataset is done using csv reader module instead of using Pandas. Due to the objective that there is no manipulation to be done on the dataset and this also eleminates the overhead caused by Pandas. 

### Inserting data to Database 
- The data is read one by one from the reader instance from the csv reader. This will not hold up a lot of RAM during the runtime. 
- Using the ORM functionality in SQLAlchemy of bulk insert, the addition of data to databse can be optimised by sending bulk data at a point in time. And then commited to the database. 
- This can be carried out for computational efficency. 

### Observations 

I have attached the usage of the RAM while doing a one by one addition of the user to the database and by doing a bulk insertion to the database. 

- One by one insertion 
![screenshot](test_images/test_screenshots/memory_random_test_big_no_bulk.png)

-Bulk insertion 
![screenshot](test_images/test_screenshots/memory_random_test_big.png)

	By doing a bulk insertion the usage of the RAM is reduced during the isertion to the database. 

- The usage of the PostgreSQL was useful in creating a local server and having an user interface to deal with the database. 
The following image indicates the raw SQL statement on the pgAdmin interface. 
![raw_sql](test_images/test_screenshots/sql_raw.png)

### Query 
- session.query(func.count(database_class.courses),database_class.name).filter_by(grade=1.0).group_by(database_class.name).having(func.count(database_class.courses)>= 3.0) 

### References 
- https://pypi.org/project/SQLAlchemy/
- https://www.tutorialspoint.com/sqlalchemy/index.htm
- https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
- https://leportella.com/sqlalchemy-tutorial.html


