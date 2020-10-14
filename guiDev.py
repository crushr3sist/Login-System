from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivymd.app import MDapp
from kivymd.uix.screen import screen
from kivy.lang import Builder


userNameAssets = '''
MDTextField:
    hint_text: "Enter Username"
    helper_text: "click forgotten username"
    helper_text_mode: "persistent"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x:None
    width:300
'''

passNameAssets = '''
MDTextField:
    hint_text: "Enter password"
    helper_text: "click forgotten password"
    helper_text_mode: "persistent"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x:None
    width:300
'''


class YourApp(MDapp):
    def build(self):

        screen = Screen()
        user_nameLabel = Label(text="Username")
        


        user_nameInp = Builder.load_string(userNameAssets)

        pass_nameLabel = Label(text="Password")
        pass_nameInp = Builder.load_string(passNameAssets)

        login = Button(text='login', width=80,height=5,pos_hint={"center_x":0.5,"center_x":0.1},size_hint_x=None)
        
        
        layout.add_widget(user_nameLabel)
        layout.add_widget(user_nameInp)
        layout.add_widget(pass_nameLabel)        
        layout.add_widget(pass_nameInp)
        layout.add_widget(login)


        return layout


YourApp().run()

