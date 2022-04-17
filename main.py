from api import *
from admin import *
import sqlite3, spriteClicked


def main():

    login_page()

    while True:
        pygame.event.pump()
        # functions
        if keyPressed("space"):
            end()
        if spriteClicked(editTableBTN):
            print("you want to edit the database")
        if spriteClicked(registerBTN):
            print("you want to register a employee")
        if spriteClicked(viewTBBTN):
            print("you want to view the database tables")
    endWait()


if __name__ == "__main__":
    main()
