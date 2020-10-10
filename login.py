from connectDB import *


def login():
    try:
        con = connect()

        login_Username = input("enter your username:")
        login_Password = input("enter your password:")

        login_attempt = con.execute('''
        SELECT userName FROM users
        SELECT password FROM users
        SELECT TOP 1 users.userName FROM users WHERE users.userName = ?
        SELECT TOP 1 users.password FROM password WHERE users.password = ?
        ''',(login_Username,login_Password))
    except Error as e:
        print(e)
    if login_attempt == True:
        print("you logged in successfully :)")

def checkIfDbIsEmpty():

    con = connect()
    checkIfEmpty = con.execute('''
    SELECT name FROM sqlite_master WHERE name='users' ''')


checkIfDbIsEmpty()
if checkIfDbIsEmpty == None:
    print("the table is empty, you cannot login")
    createTableFormat()
    

    

