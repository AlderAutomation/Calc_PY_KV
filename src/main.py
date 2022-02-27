from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMenu, QMenuBar, QAction
from PyQt5 import uic
import sys
 

class main_ui_window(QMainWindow):
    def __init__(self) -> None:
        super(main_ui_window, self).__init__()

        uic.loadUi("./gui/calc.ui", self)

        self.operator = ""
        self.stored = 0
        self.is_equaled = False

        #define UI
        self.display_label = self.findChild(QLabel, "display_label")
        self.C_button = self.findChild(QPushButton, "C_button")
        self.CE_button = self.findChild(QPushButton, "CE_button")

        self.button_1 = self.findChild(QPushButton, "button_1")
        self.button_2 = self.findChild(QPushButton, "button_2")
        self.button_3 = self.findChild(QPushButton, "button_3")
        self.button_4 = self.findChild(QPushButton, "button_4")
        self.button_5 = self.findChild(QPushButton, "button_5")
        self.button_6 = self.findChild(QPushButton, "button_6")
        self.button_7 = self.findChild(QPushButton, "button_7")
        self.button_8 = self.findChild(QPushButton, "button_8")
        self.button_9 = self.findChild(QPushButton, "button_9")
        self.button_0 = self.findChild(QPushButton, "button_0")
        # self.decimal_button = self.findChild(QPushButton, "decimal_button")
        
        self.divide_button = self.findChild(QPushButton, "divide_button")
        self.multiply_button = self.findChild(QPushButton, "multiply_button")
        self.subtraction_button = self.findChild(QPushButton, "subtraction_button")
        self.addition_button = self.findChild(QPushButton, "addition_button")
        self.equals_button = self.findChild(QPushButton, "equals_button")

        #assign Actions 
        self.C_button.clicked.connect(self.clear)
        self.CE_button.clicked.connect(self.clear_entry)
        self.button_1.clicked.connect(lambda: self.button_number(1))
        self.button_2.clicked.connect(lambda: self.button_number(2))
        self.button_3.clicked.connect(lambda: self.button_number(3))
        self.button_4.clicked.connect(lambda: self.button_number(4))
        self.button_5.clicked.connect(lambda: self.button_number(5))
        self.button_6.clicked.connect(lambda: self.button_number(6))
        self.button_7.clicked.connect(lambda: self.button_number(7))
        self.button_8.clicked.connect(lambda: self.button_number(8))
        self.button_9.clicked.connect(lambda: self.button_number(9))
        self.button_0.clicked.connect(lambda: self.button_number(0))
        # self.decimal_button.clicked.connect(lambda: self.button_number("."))
        self.divide_button.clicked.connect(lambda: self.operation("divide"))
        self.multiply_button.clicked.connect(lambda: self.operation("multiply"))
        self.subtraction_button.clicked.connect(lambda: self.operation("subtract"))
        self.addition_button.clicked.connect(lambda: self.operation("add"))
        self.equals_button.clicked.connect(self.equals)

        self.show()
    

    def clear(self):
        self.display_label.setText("0")
        self.operator = ""
        self.stored = 0

 
    def clear_entry(self):
        self.display_label.setText("0")


    def backspace(self):
        pass


    def operation(self, operator):
        self.stored = self.display_label.text()
        self.operator = operator
        self.display_label.setText("0")


    def equals(self):
        if self.operator == "add":
            result = int(self.stored) + int(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "subtract":
            result = int(self.stored) - int(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "divide":
            result = int(self.stored) / int(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True
        elif self.operator == "multiply":
            result = int(self.stored) * int(self.display_label.text())
            self.display_label.setText(str(result))
            self.is_equaled = True


    def button_number(self, num):
        if self.is_equaled is True:
            self.display_label.setText("0") 
            self.is_equaled = False           

        if self.display_label.text() == "0":
            self.display_label.clear()
            self.display_label.setText(str(num))
        else:
            existing_num = self.display_label.text()
            new_num = str(existing_num) + str(num)
            new_num = int(new_num)
            self.display_label.setText(str(new_num))


def main():
    app = QApplication(sys.argv)
    UIWindow = main_ui_window()
    app.exec_()


if __name__=="__main__":
    main()