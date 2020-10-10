from connectDB import *

def createTableFormat():
    # declaring a variable which connects to the database 
    conn = connect()
    # this is a query which creates a table, this specific query sets up the table's format
    conn.execute('''
        CREATE TABLE users (
            userID int,
            firstName varchar(255),
            lastName varchar(255),
            email varchar(255),
            userName varchar(255),
            password varchar(255)
        )
        ''')

    # this functions applies the query to the connected database 
    conn.commit()
    # this saves and closes the database
    conn.close()
    



