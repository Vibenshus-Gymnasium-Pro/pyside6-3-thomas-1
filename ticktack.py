

turn = 0

def tick_or_tack(turn, button):
    if turn%2 == 0:
        change_button(button, "X")
        turn += 1
    else:
        change_button(button, "O")
        turn += 1

def change_button(button, symbol):



lambda checked: self.handle_trigger(checked, turn)