
X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
O = [0, 0, 0, 0, 0, 0, 0, 0, 0]

WINS = [[1,1,1,0,0,0,0,0,0], [0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,1,1,1], [1,0,0,1,0,0,1,0,0], [0,1,0,0,1,0,0,1,0], [0,0,1,0,0,1,0,0,1], [1,0,0,0,1,0,0,0,1], [0,0,1,0,1,0,1,0,0]]




def reset():
    global X, O
    X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    O = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def check_win():
    
    for win in WINS:
        index = 0
        X_hits = 0
        O_hits = 0
        for spot in win:
            if X[index] and spot:
                X_hits += 1
            if O[index] and spot:
                O_hits += 1
            
            if X_hits >= 3:
                return "X"
            
            if O_hits >= 3:
                return "O"

            index += 1

                
