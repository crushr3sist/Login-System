import sqlite3
from sqlite3 import Error
import os

def register():
    con = connect()
    try:
        userID = 0
        userID = userID + 1
        firstName = str(input("enter your first name:"))
        lastName = str(input("enter your last name:"))
        emailAdd = str(input(r"enter your email address:"))
        userName = str(input("enter your desired username:"))
        password = str(input("enter your desired password:"))
        con.execute('''
        INSERT INTO users (userID,firstName,lastName,email,userName,password)
        VALUES (?,?,?,?,?,?)''',
        (userID, firstName, lastName, emailAdd,userName,password)
        )
        con.commit()
        con.close()
        print("your account has been created :)")
    except Error as e:
        print(e)

def login():
    try:
        con = connect()
        login_Username = input("enter your username:")
        login_Password = input("enter your password:")
        con.execute("SELECT userName, password FROM users")
        cursor = con.cursor()
        fetchAuthData = list(cursor.fetchall())
        if login_Password not in fetchAuthData or login_Username not in fetchAuthData:
            for i in range(0,6):
                print("please try again")
                login_Username = input("enter your username:")
                login_Password = input("enter your password:")
                if login_Password not in fetchAuthData or login_Username not in fetchAuthData:
                    print("login sucessful")
                    break
                else:
                    if i >= 5:
                        print("please try again later")
                        break
        if login_Password in fetchAuthData and login_Username in fetchAuthData:
            print("Login Sucessful")            
    except Error as e:
        print(e)

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
            password varchar(255),

            employeeID int,
            shiftStatus boolean,
            Age int,
            Wage int,
            position varchar(255)
        )
        ''')
    conn = connect()
    Cursor = conn.cursor()
    Cursor.execute("SELECT COUNT(*) from users")
    resultFetch = list(Cursor.fetchall())
    if resultFetch == None or False:
        print("table is empty")
    conn.commit()
    conn.close()
    
def connect():
    Path = os.getcwd()+"\main_DataBase.db"
    try:
        if Path != os.path.islink(Path):
            con = sqlite3.connect(Path)
        if os.path.exists(Path) == True:
            #print("database is being created or already exists")
            None
        elif os.path.exists(Path) == False:
            print(fr"Your was created successfully at {os.getcwd()+'/main_DataBase.db'} ")
    except OSError as errormsg:
        print(errormsg+"\n"+"The file couldn't be created, please relocate the python file to the desktop")
    except Error as e:
        print(e)        
    return con