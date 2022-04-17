from pygame_functions import *
from sqlite3 import Error
from api import connect

window_x = 1280
window_y = 720

screenSize(window_x, window_y)

background = (126, 164, 179)
message_color = ((126 - 80), (164 - 80), (179 - 80))
login_button = makeSprite("buttons/login.png")
register_button = makeSprite("buttons/register.png")
main_page_message = makeLabel(
    "Would you like to Login or Register Please click the corresponding Button",
    36,
    100,
    100,
    message_color,
    "Segoe UI",
)
login_page_message = makeLabel(
    "please type your username and password, make sure you are a administrator",
    36,
    100,
    100,
    message_color,
    "Segoe UI",
)
login_page_userName_message = makeLabel(
    "type your username below", 36, 100, 250, message_color, "Segoe UI"
)
login_page_password_message = makeLabel(
    "type your password below", 36, 100, 450, message_color, "Segoe UI"
)


def login_page():

    hideAll()
    hideLabel(main_page_message)
    showLabel(login_page_message)
    setBackgroundColour(background)

    session_admin = False
    session_user = False

    try:
        # con = connect()
        showLabel(login_page_userName_message)
        showLabel(login_page_password_message)
        login_Username_textbox = makeTextBox(
            100, 350, 500, 0, "enter your username:", 99, 25
        )
        login_Password_textbox = makeTextBox(
            100, 550, 500, 0, "enter your password:", 99, 25
        )

        login_Username = textBoxInput(login_Username_textbox)
        login_Password = textBoxInput(login_Password_textbox)

        con.execute("SELECT userName, password FROM Users,Admin ")
        cursor = con.cursor()
        fetchAuthData = list(cursor.fetchall())

        print(fetchAuthData)

        if login_Password not in fetchAuthData or login_Username not in fetchAuthData:
            for i in range(0, 6):
                print("please try again")
                login_Username = input("enter your username:")
                login_Password = input("enter your password:")
                if login_Password in fetchAuthData or login_Username in fetchAuthData:
                    # check if the entered details belong in the admin or user table
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


login_page()


# this function is for the admin page. keep in development
def main_page():
    moveSprite(login_button, ((window_x / 2) - 118) + 70, ((720 / 2) - 50) + 20)
    moveSprite(register_button, ((window_x / 2) - 118) + 70, ((720 / 2) - 50) + 200)
    showSprite(login_button)
    showSprite(register_button)
    setBackgroundColour(background)
    transformSprite(login_button, 0, 1.5)
    transformSprite(register_button, 0, 1.5)
    showLabel(main_page_message)
