import sqlite3
from sqlite3 import Error
import os
from database import *
#from Interface import guiDev

def main():
    try:
        connectionChoice = input("would you like to login or register\n:")
        if connectionChoice == "login":
            login()
        if connectionChoice == "register":
            register()
    except Error as e:
        print(e)
        pass


