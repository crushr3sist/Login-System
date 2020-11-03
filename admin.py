from pygame_functions import *

# def init_admin():
screenSize(1290,720)
background = (126, 164, 179)
message_color = ((126-80), (164-80), (179-80))
setBackgroundColour(background)
main_page_message = makeLabel("Admin Access",36,590,45,message_color,'Segoe UI')
spriteX = 40
spriteY = 40
speed = 1

editTableBTN = makeSprite('buttons/edit.png')
edit_table = makeLabel("Edit Table",36,470,154,message_color,'Segoe UI')
moveSprite(editTableBTN,590,121)

registerBTN = makeSprite('buttons/register.png')
Register = makeLabel("Register Employee",36,604,325,message_color,'Segoe UI')
moveSprite(registerBTN,495,290)

viewTBBTN = makeSprite('buttons/viewTB.png')
viewDatabase = makeLabel("View Database",36,485,490,message_color,'Segoe UI')
moveSprite(viewTBBTN,695,455)

showSprite(registerBTN)
showSprite(editTableBTN)
showSprite(viewTBBTN)

transformSprite(registerBTN,0,0.5)
transformSprite(editTableBTN,0,0.5)
transformSprite(viewTBBTN,0,0.7)
showLabel(edit_table)
showLabel(Register)
showLabel(viewDatabase)
showLabel(main_page_message)

# init_admin()

while True:
    pygame.event.pump()
    if keyPressed('space'):
        end()
endWait()



# def admin_init():

#     pass