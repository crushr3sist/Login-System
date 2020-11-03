from pygame_functions import *

def init_admin():
    screenSize(1290,720)
    background = (126, 164, 179)
    message_color = ((126-80), (164-80), (179-80))
    setBackgroundColour(background)
    main_page_message = makeLabel("Admin Acess",36,590,45,message_color,'Segoe UI')

    edit_table = makeLabel("Edit Table",36,50,90,message_color,'Segoe UI')
    Register = makeLabel("Register Employee",36,50,265,message_color,'Segoe UI')
    viewDatabase = makeLabel("View Database",36,50,420,message_color,'Segoe UI')

    showLabel(edit_table)
    showLabel(Register)
    showLabel(viewDatabase)
    
    showLabel(main_page_message)
    viewTBBTN = makeSprite('buttons/viewTB.png')
    registerBTN = makeSprite('buttons/register.png')
    editTableBTN = makeSprite('buttons/edit.png')
    loginBTN = makeSprite('buttons/login.png')

    moveSprite(viewTBBTN,60,120)
    moveSprite(registerBTN,60,295)
    moveSprite(editTableBTN,60,480)

    showSprite(viewTBBTN)
    showSprite(registerBTN)
    showSprite(editTableBTN)

    transformSprite(viewTBBTN,0,0.7)
    transformSprite(registerBTN,0,0.5)
    transformSprite(editTableBTN,0,0.5)


init_admin()

while True:
    pygame.event.pump()
    if keyPressed('space'):
        break
endWait()


def admin_init():


    pass