from tableFormat import *
from sqlite3 import Error


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

