from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMenu, QMenuBar, QAction, QDialog, QShortcut
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
import sys
import pyperclip
 
app_version = 0.001

class main_ui_window(QMainWindow):
    def __init__(self) -> None:
        super(main_ui_window, self).__init__()

        uic.loadUi("./gui/calc.ui", self)

        self.operator = ""
        self.stored = 0
        self.is_equaled = False

        # Shortcuts
        self.shortcut_copy = QShortcut(QKeySequence('Ctrl+C'), self)
        self.shortcut_copy.activated.connect(self.copy)
        self.shortcut_paste = QShortcut(QKeySequence('Ctrl+V'), self)
        self.shortcut_paste.activated.connect(self.paste)
        
        #define UI
        self.action_about = self.findChild(QAction, "action_about")
        self.action_copy = self.findChild(QAction, "actionCopy")
        self.action_paste = self.findChild(QAction, "actionPaste")
        self.display_label = self.findChild(QLabel, "display_label")
        self.C_button = self.findChild(QPushButton, "C_button")
        self.CE_button = self.findChild(QPushButton, "CE_button")
        self.backspace_button = self.findChild(QPushButton, "backspace_button")
        self.percent_button = self.findChild(QPushButton, "percent_button")
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
        self.decimal_button = self.findChild(QPushButton, "decimal_button")
        self.divide_button = self.findChild(QPushButton, "divide_button")
        self.multiply_button = self.findChild(QPushButton, "multiply_button")
        self.subtraction_button = self.findChild(QPushButton, "subtraction_button")
        self.addition_button = self.findChild(QPushButton, "addition_button")
        self.equals_button = self.findChild(QPushButton, "equals_button")

        #assign Actions 
        self.action_about.triggered.connect(self.about_screen)
        self.action_copy.triggered.connect(self.copy)
        self.action_paste.triggered.connect(self.paste)
        self.C_button.clicked.connect(self.clear)
        self.CE_button.clicked.connect(self.clear_entry)
        self.backspace_button.clicked.connect(self.backspace)
        self.percent_button.clicked.connect(self.percent)
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
        self.decimal_button.clicked.connect(self.decimal)
        self.divide_button.clicked.connect(lambda: self.operation("divide"))
        self.multiply_button.clicked.connect(lambda: self.operation("multiply"))
        self.subtraction_button.clicked.connect(lambda: self.operation("subtract"))
        self.addition_button.clicked.connect(lambda: self.operation("add"))
        self.equals_button.clicked.connect(self.equals)

        self.about = about_window()

        self.show()
    

    def about_screen(self) -> None:
        self.about.show()

    
    def copy(self) -> None:
        pyperclip.copy(self.display_label.text())


    def paste(self) -> None:
        try:
            if float(pyperclip.paste()) or int(pyperclip.paste()):
                self.display_label.setText(pyperclip.paste())
        except ValueError as e:
            print (e)
    

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


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



class about_window(QDialog):
    def __init__(self) -> None:
        super(about_window, self).__init__()

        uic.loadUi("./gui/about.ui", self)


def main() -> None:
    app = QApplication(sys.argv)
    UIWindow = main_ui_window()
    app.exec_()


if __name__=="__main__":
    main()

    