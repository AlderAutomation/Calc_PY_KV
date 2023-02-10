import os, sys, subprocess
from threading import Thread
import math
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.text import LabelBase

cwd = os.getcwd()
kivy.require("1.9.1")
Config.set('kivy', 'log_dir', cwd + "/logs/")
Config.set('kivy', 'log_level', 'debug')
Config.write()
# LabelBase.register(name='digital7', fn_regular= cwd + '/assets/fonts/Digital7.ttf')

class main_ui_window(BoxLayout):
    calc_label = StringProperty()
    buttonbg = .4,.4,.6,1

    def __init__(self, **kwargs):
        super(main_ui_window, self).__init__(**kwargs)
        self.calc_label = "0"
        self.not_equaled = True
        self.stored = ""


    def update_label(self, button:str):
        if self.not_equaled:
            if self.calc_label == "0":
                self.calc_label = button
            else:
                self.calc_label = self.calc_label + button
        else: 
            self.not_equaled = True
            self.calc_label = button


    def operator(self, operator:str):
        if self.stored == "":
            self.stored = self.calc_label + operator
            self.calc_label = "0"
        else:
            self.stored = self.stored + self.calc_label + operator
            self.calc_label = "0"


    def backspace(self) -> None:
        if len(self.calc_label) <= 1:
            self.calc_label = "0"
        else:
            self.calc_label = self.calc_label[:-1]

    def reset(self) -> None: 
        self.calc_label = "0"
        self.stored = ""


    def percent(self) -> None:
        num_of_percent = float(self.calc_label)
        self.calc_label = str(num_of_percent / 100)


    def square(self) -> None: 
        self.calc_label = str(math.sqrt(int(self.calc_label)))


    def equals(self) -> None:
        self.stored = self.stored + self.calc_label
        self.calc_label = str(eval(self.stored))
        self.stored = ""
        self.not_equaled = False

    
    def decimal(self) -> None:
        to_dec_num = self.display_label.text()
        
        if "." in to_dec_num:
            pass
        else:
            self.display_label.setText(to_dec_num + ".")        


    @staticmethod
    def open_about_window():
        Thread(target=lambda *largs: subprocess.run([sys.executable, cwd + "/src/about.py"])).start()


class MainApp(App):
    def build(self):
        self.icon = cwd + "/assets/pics/calculator.png"
        return main_ui_window()



if __name__=="__main__":
    
    MainApp().run()