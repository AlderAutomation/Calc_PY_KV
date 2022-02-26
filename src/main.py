from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMenu, QMenuBar, QAction
from PyQt5 import uic
import sys
 

class main_ui_window(QMainWindow):
    def __init__(self) -> None:
        super(main_ui_window, self).__init__()

        uic.loadUi("./gui/calc.ui", self)

        #define UI
        self.display_label = self.findChild(QLabel, "display_label")
        self.C_button = self.findChild(QPushButton, "C_button")

        self.button_1 = self.findChild(QPushButton, "button_1")
        self.button_2 = self.findChild(QPushButton, "button_2")
        
        self.addition_button = self.findChild(QPushButton, "addition_button")
        self.equals_button = self.findChild(QPushButton, "equals_button")

        #assign Actions 
        self.C_button.clicked.connect(self.clear)
        self.button_1.clicked.connect(lambda: self.number(1))
        self.button_2.clicked.connect(lambda: self.number(2))
        self.addition_button.clicked.connect(self.addition)
        self.equals_button.clicked.connect(lambda: self.equals(99))

        self.show()
    

    def equals(self, answer):
        self.display_label.setText(str(answer))


    def addition(self):
        pass


    def number(self, num):
        if self.display_label.text() is "0":
            self.display_label.clear()
            self.display_label.setText(str(num))
        else:
            existing_num = self.display_label.text()
            new_num = str(existing_num) + str(num)
            new_num = int(new_num)
            self.display_label.setText(str(new_num))


    def clear(self):
        self.display_label.setText("0")


def main():
    app = QApplication(sys.argv)
    UIWindow = main_ui_window()
    app.exec_()


if __name__=="__main__":
    main()