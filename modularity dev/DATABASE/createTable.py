from connecttodatabase import *
class create_table:
    def __init__(self):
        self.conn = self.establish()
        self.Cursor = conn.cursor()
        self.resultFetch = list(Cursor.fetchall())
    def createTableFormat():
        self.conn.execute('''
            CREATE TABLE users (
                userID int,
                firstName varchar(255),
                lastName varchar(255),
                email varchar(255),
                userName varchar(255),
                password varchar(255),

                employeeID int,
                shiftStatus boolean,
                Age int,
                Wage money,
                position varchar(255)
            )
            ''')
        self.Cursor.execute("SELECT COUNT(*) from users")
        if self.resultFetch == None or False:
            print("table is empty")
        self.conn.commit()
        self.conn.close()
