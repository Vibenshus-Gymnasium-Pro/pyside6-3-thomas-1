import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject


loader = QUiLoader()





class Tictactoe(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("ticktacktoe.ui", None)
        self.turn = 0
        self.btnlist = []
        
        
        
        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters. NOTE Not done
        self.buttons = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]
        for a in self.buttons:
            a.clicked.connect(lambda checked, val=a : self.pressed(val))
        
    

    def pressed(self, button):
        if len(self.btnlist) >= 9:
            self.clear()
            return
        print("Worked")
        print(button)
        if button not in self.btnlist:
            if self.turn % 2 == 0:
                button.setText("X")
                self.btnlist.append(button)
                self.turn += 1
            elif self.turn %2 == 1:
                button.setText("O")
                self.btnlist.append(button)
                self.turn += 1

    def clear (self):

        for i in self.btnlist:
            i.setText("")
        self.btnlist = []
        



program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()