import sys, os
import pyperclip
import math
import kivy
from kivy.app import App
from kivy.logger import Logger
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout

cwd = os.getcwd()
kivy.require("1.9.1")
Config.set('kivy', 'log_dir', cwd + "/logs/")
Config.set('kivy', 'log_level', 'debug')
Config.write()

class main_ui_window(GridLayout):
    def about_screen(self) -> None:
        # self.about.show()
        print("Make an About screen")
    

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()


    def clear(self) -> None:
        self.display_label.setText("0")
        self.operator = ""
        self.stored = 0

 
    def clear_entry(self) -> None:
        self.display_label.setText("0")


    def backspace(self) -> None:
        templabel = self.display_label.text()
        self.display_label.setText(templabel[:-1])        


    def operation(self, operator: str) -> None:
        self.stored = self.display_label.text()
        self.operator = operator
        self.display_label.setText("0")


    def equals(self) -> None:
        if self.operator == "add":
            result = float(self.stored) + float(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "subtract":
            result = float(self.stored) - float(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "divide":
            result = float(self.stored) / float(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "multiply":
            result = float(self.stored) * float(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True


    def button_number(self, num: float) -> None:
        if self.is_equaled is True:
            self.display_label.setText("0") 
            self.is_equaled = False           

        if self.display_label.text() == "0":
            self.display_label.clear()
            self.display_label.setText(str(num))
        else:
            existing_num = self.display_label.text()
            new_num = str(existing_num) + str(num)
            self.display_label.setText(str(new_num))

    
    def percent(self) -> None:
        num_of_percent = float(self.display_label.text())
        percent_in_decimal = num_of_percent / 100
        self.display_label.setText(str(percent_in_decimal * float(self.stored)))

    
    def decimal(self) -> None:
        to_dec_num = self.display_label.text()
        
        if "." in to_dec_num:
            pass
        else:
            self.display_label.setText(to_dec_num + ".")        


# class about_window(QDialog):
#     def __init__(self) -> None:
#         super(about_window, self).__init__()

#         uic.loadUi("./gui/about.ui", self)


class MainApp(App):
    def build(self):
        return main_ui_window()


if __name__=="__main__":
    MainApp().run()