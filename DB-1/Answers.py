""" 1) Database is collection of data or records. 
    a) SQL is Structured query language and the Databases of 
these type are typically stored in Relational format (represented in tabular form).
         SQL is the language used to work on the tabular database.
    b) NOSQL is not only SQL where we have other databse format like key,value pairs, documents,graph format


    2) DDL is data definition language in SQL where we can define the database schema. 
        a) create - create a database table
        eg- create table student(stud_name varchar(20), stud_id int(4), stud_standard int(2));

        b) drop - drops or deletes the table 
        eg- drop table student;

        c) alter - changes the table structure like type of data, number of columns, column size
        eg- alter table student add (age int(3), course int(10));

        d) truncate- deletes all the data inside the table. 
        eg - truncate table student;

    3) DML is data manipulation language which is used to modify the data of the tables.

        a) insert - inserts values into table as row
        eg - insert into student values ("Chintu", 1003,9, 14, "Higher secondary");

        b) update - updates values of a particular row, needs a where clause for finding exact rows that needs to be updated.
        eg - update student set stud_name="Pintu" where stud_id =1003;

        c) delete - deletes rows from given table, needs a where clause for finding exact row that needs to be updated.
        eg - delete from student where stud_id=001; 


    4) DQL is data query language which is used for querying the table
        eg- select * from student where stud_id=001;    

    5) Primary key is a column or multiple columns used to identify the record or row uniquely. 
       Foreign key-  primary key from one table which is used in another table as foreign key.

    6) DBConnection.py file 
import mysql.connector
import logging

class DBConnect:

    def __init__(self):
        print("Creating DB Connection")
        logging.basicConfig(filename='DB.log',  level=logging.DEBUG)
        


    def estdbconnection(self):

        try:
            db=mysql.connector.connect(
                host="localhost",
                user="abc",
                password="password")
                
        except Exception as e:
            logging.exception("DB Connection Exception",e)
        
        return db


##### DB1.py file
import DBConnection


conn = DBConnection.DBConnect()
myconnection = conn.estdbconnection()

mycursor=myconnection.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

        
    7)  1) from - choose and join tables to get the base data
        2) where - filters based on data
        3) group by - aggregates the base data
        4) having - filters the aggregated data
        5) select - returns the final data
        6) order by - sorts the final data
        7) limit- limits the returned data to a row count
"""