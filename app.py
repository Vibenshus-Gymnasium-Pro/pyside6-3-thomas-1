import sys
import ticktack

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
        self.won = False
        self.cross = True
        self.x_won = 0
        self.o_won = 0
        
        
        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters.
        self.buttons = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]
        for a in self.buttons:
            a.clicked.connect(lambda checked, val=a : self.pressed(val))
        self.update_status()
        
        
        
    

    def pressed(self, button):
        # checks if all buttons have been pressed, if so clears
        if self.won == True:
            self.clear
            self.won = False
            return
        if len(self.btnlist) >= 9:
            self.clear()
            return
        
        
        
        print("Worked")
        print(button)
        # Checks if button has been pressed or not
        if button not in self.btnlist:
            # Checks whose turn it is, and then writes the coresponding symbol
            if self.cross:
                button.setText("X")
                
                
            else:
                button.setText("O")
                
            self.btnlist.append(button)
            self.cross = not self.cross
            self.update_status()
           
                
        

    def update_status(self):
        if self.cross:
            self.ui.win.setText("X turn")
        else:
            self.ui.win.setText("O turn")
        if ticktack.check_win() == "O":
            self.ui.win.setText("O Won!")
            self.o_won += 1
            self.won = True

        if ticktack.check_win() == "X":
            self.ui.win.setText("X Won!")
            self.x_won += 1
            self.won = True
        if len(self.btnlist) >= 9:
            self.ui.win.setText("Tie")
        

        self.ui.O_score.setText(f"O Wins: {self.o_won}")
        self.ui.X_score.setText(f"X Wins: {self.x_won}")

    def clear (self):
        # Loops through the buttons, clearing them
        for i in self.btnlist:
            i.setText("")
        self.btnlist = []
        ticktack.reset()
        if self.cross:
            self.ui.win.setText("X turn")
        else:
            self.ui.win.setText("O turn")
        
    
    
        


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()