
X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
O = [0, 0, 0, 0, 0, 0, 0, 0, 0]

WINS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]




def reset():
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

                


check_win()