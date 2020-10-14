import sqlite3
from sqlite3 import Error
import os

from api import *

def main():

    try:

        connectionChoice = input("would you like to login or register\n:")
        if connectionChoice == "login":
            createTableFormat()
            login()
        if connectionChoice == "register":
            register()
    except Error as e:
        print(e)
        pass


