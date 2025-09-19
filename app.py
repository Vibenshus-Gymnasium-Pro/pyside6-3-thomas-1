import sys
import ticktack
import logic
import time
import rand_logic


from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject


loader = QUiLoader()





class Tictactoe(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("ticktacktoe.ui", None)
        self.btnlist = []
        self.won = False
        self.cross = True
        self.x_won = 0
        self.o_won = 0
        self.rand_ai = False
        self.hard_ai = False
        self.ai_player = False
        
        
        # Creating a list of all the buttons, for use in the for loop connecting them all to the same slot with different parameters.
        self.buttons = [self.ui.button1, self.ui.button2, self.ui.button3, self.ui.button4, self.ui.button5, self.ui.button6, self.ui.button7, self.ui.button8, self.ui.button9]
        for a in self.buttons:
            a.clicked.connect(lambda checked, val=a : self.pressed(val))
        self.update_status()

        
        
       
        self.ui.randomAI.clicked.connect(self.ai_bool)
        self.ui.goodAI.clicked.connect(self.hard_ai_bool)
        
    def ai_bool(self):
        print("test")
        self.rand_ai = not self.rand_ai
        self.ai_player = not self.ai_player
    
    def hard_ai_bool(self):
        print("test_hard")
        self.hard_ai = not self.hard_ai
        self.ai_player = not self.ai_player
    

    def pressed(self, button):
        # checks if all buttons have been pressed, if so clears
        if self.won == True:
            self.clear()
            return

        # Checks if button has been pressed or not
        if self.ai_player == False:
            if button not in self.btnlist:
            # Checks whose turn it is, and then writes the coresponding symbol
                if self.cross:
                    button.setText("X")
                    ticktack.X[self.buttons.index(button)] = 1
                    self.cross = not self.cross
                    
                    
                else:
                    button.setText("O")
                    ticktack.O[self.buttons.index(button)] = 1
                    self.cross = not self.cross
                
                self.btnlist.append(button)
        elif self.ai_player == True:
            if self.hard_ai == True:
                if self.cross:
                    if button not in self.btnlist:
                        button.setText("X")
                        ticktack.X[self.buttons.index(button)] = 1
                        self.btnlist.append(button)
                        self.cross = not self.cross
                        self.hard_ai_press()
                    
                
            elif self.rand_ai == True:
                if self.cross:
                    if button not in self.btnlist:
                        button.setText("X")
                        ticktack.X[self.buttons.index(button)] = 1
                        self.btnlist.append(button)
                        self.cross = not self.cross
                        self.ai_press()

        
                    
            
        self.update_status()
            
    
    def ai_press(self):
        button = rand_logic.pick_square(self.buttons)
        if len(self.btnlist) < 9:
            if button not in self.btnlist:
                button.setText("O")
                ticktack.O[self.buttons.index(button)] = 1
                self.btnlist.append(button)
                self.cross = not self.cross
                return
            else:
                self.ai_press()
            
    def hard_ai_press(self):
        move = logic.best_move("O")
        if move is not None:
            button = self.buttons[move]
            if button not in self.btnlist:
                button.setText("O")
                ticktack.O[move] = 1
                self.btnlist.append(button)
                self.cross = not self.cross
                
        

    def update_status(self):
        # Checks whose turn it is, and updates the UI to reflect it
        if self.cross:
            self.ui.win.setText("X turn")
        else:
            self.ui.win.setText("O turn")
        
        # Checks if someone has won, changes the UI to reflect it and adds to the score
        if ticktack.check_win() == "O":
            self.ui.win.setText("O Won!")
            self.o_won += 1
            self.won = True
        elif ticktack.check_win() == "X":
            self.ui.win.setText("X Won!")
            self.x_won += 1
            self.won = True

        # If all 9 squares have been filled without a win, then declares it as a tie
        if len(self.btnlist) >= 9 and self.won == False:
            self.won = True
            self.ui.win.setText("Tie")

        
            
        
        # Updates the players scores in the UI
        self.ui.O_score.setText(f"O Wins: {self.o_won}")
        self.ui.X_score.setText(f"X Wins: {self.x_won}")

    def clear (self):
        # Loops through the buttons, clearing them
        for i in self.btnlist:
            i.setText("")
        self.btnlist = []
        # Resets the backend ressources
        ticktack.reset()
        logic.reset()

        # Changes the UI to reflect who starts
        if self.cross:
            self.ui.win.setText("X turn")
        else:
            self.ui.win.setText("O turn")

        self.won = False
        
    

        


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
tictactoe = Tictactoe()
tictactoe.ui.show()
program.exec()