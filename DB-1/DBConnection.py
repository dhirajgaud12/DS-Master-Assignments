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