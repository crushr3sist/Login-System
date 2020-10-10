import sqlite3
from sqlite3 import Error
import os

def connect():
    Path = os.getcwd()+"\main_DataBase.db"
    try:
        if Path != os.path.islink(Path):
            con = sqlite3.connect(Path)
            
        if os.path.exists(Path) == True:
            print("database is being created or already exists")
        elif os.path.exists(Path) == False:
            print(fr"Your was created successfully at {os.getcwd()+'/main_DataBase.db'} ")
    except OSError as errormsg:
        print(errormsg+"\n"+"The file couldn't be created, please relocate the python file to the desktop")
    except Error as e:
        print(e)        
    return con

connect()