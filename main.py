from signup import *
from login import *

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


if __name__ == "__main__":
    main()



