import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject


loader = QUiLoader()


class Tictactoe(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("ticktacktoe.ui", None)

        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters. NOTE Not done
        self.buttons = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]
        for a in self.buttons:
            a.clicked.connect(lambda val=a : self.pressed(val))

    def pressed(self, button):
        print("Worked")
        print(button)


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()