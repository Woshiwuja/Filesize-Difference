import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import numpy as np
from numpy import random
import string


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Peer ID'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

    def randomSecureString():
        string_size = 24
        for i in range(string_size):
            ran = np.random.randint(0,255)

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
