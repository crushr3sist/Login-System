import sqlite3
from sqlite3 import Error
import os


def admin_register():
    con = connect()
    try:
        con.execute(
            """
            INSERT INTO Admin (email,userName,password) VALUES (?,?,?)
        """,
            ("Wizock.Admin@mail.com", "WizockAdmin", "Admin123"),
        )
        con.commit()
        con.close()
        print("your Admin account has been created :)")
    except Error as e:
        print(e)


def user_register():
    con = connect()
    try:
        firstName = str(input("enter your first name:"))
        lastName = str(input("enter your last name:"))
        emailAdd = str(input("enter your email address:"))
        userName = str(input("enter your desired username:"))
        password = str(input("enter your desired password:"))
        con.execute(
            """
        INSERT INTO Users (firstName,lastName,email,userName,password)
        VALUES (?,?,?,?,?)""",
            (firstName, lastName, emailAdd, userName, password),
        )
        con.execute(
            """
            INSERT INTO Admin (email,userName,password) VALUES (?,?,?)
        """,
            ("Wizock.Admin@mail.com", "WizockAdmin", "Admin123"),
        )
        con.commit()
        con.close()
        print("your account has been created :)")
    except Error as e:
        print(e)


def createTableFormat():
    # declaring a variable which connects to the database
    conn1 = connect()

    # else:
    try:
        conn1.execute(
            """        
            CREATE TABLE workers (
                firstName varchar(255),
                lastName varchar(255),
                email varchar(255),
                userName varchar(255),
                password varchar(255),
                shiftStatus boolean,
                Age int,
                Wage int,
                position varchar(255),
                employeeID INT,
                FOREIGN KEY (employeeID) REFERENCES Admin(UserId)
                )
	
            """
        )

        conn1.execute(
            """
            CREATE TABLE Admin (
                UserId INTEGER PRIMARY KEY,
                email varchar(255),
                userName varchar(255),
                password varchar(255)
                )
                """
        )
        # this is a query which creates a table, this specific query sets up the table's format
        check_Admin = conn1.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='Admin'"
        )
        check_Workers = conn1.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='workers'"
        )

        if check_Admin != None:
            conn1.execute("DROP TABLE Admin")
        if check_Workers != None:
            conn1.execute("DROP TABLE workers")
    except Error as e:
        print(e)


def connect():
    Path = os.getcwd() + "\main_DataBase.db"
    try:
        if Path != os.path.islink(Path):
            con = sqlite3.connect(Path)
            print(
                rf"Your was created successfully at {os.getcwd()+'/main_DataBase.db'} "
            )
    except OSError as errormsg:
        print(
            errormsg
            + "\n"
            + "The file couldn't be created, please relocate the python file to the desktop"
        )
    except Error as e:
        print(e)
    return con


def checkIfEmpty():
    Path = os.getcwd() + "\main_DataBase.db"
    if os.path.exists(Path) == True:
        return True
    else:
        return False
