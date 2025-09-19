# logic.py
import ticktack

def get_board():
    """Lav et bræt som en liste med 'X','O','.'"""
    board = []
    for i in range(9):
        if ticktack.X[i]:
            board.append("X")
        elif ticktack.O[i]:
            board.append("O")
        else:
            board.append(".")
    return board  # <— VIGTIGT!


_tt = {}  # fx din transposition table

def reset():
    # ryd egne caches
    _tt.clear()

    # ryd evt. lru_cache-dekorerede funktioner
    try:
        minimax.cache_clear()  # hvis du har @lru_cache på minimax
    except Exception:
        pass

def winner_of(board):
    """Returner 'X', 'O' eller None"""
    wins = [
        [0,1,2],[3,4,5],[6,7,8],   # rækker
        [0,3,6],[1,4,7],[2,5,8],   # kolonner
        [0,4,8],[2,4,6]            # diagonaler
    ]
    for line in wins:
        a,b,c = line
        if board[a] != "." and board[a] == board[b] == board[c]:
            return board[a]
    return None

def available_moves(board):
    return [i for i,v in enumerate(board) if v == "."]

def is_terminal(board):
    return winner_of(board) is not None or "." not in board

def score(board, ai_player):
    w = winner_of(board)
    if w == ai_player:
        return 1
    elif w is None:
        return 0
    else:
        return -1

def opponent(player):
    return "O" if player == "X" else "X"

def minimax(board, current_player, ai_player):
    """Returner (værdi, bedste_træk)"""
    if is_terminal(board):
        return score(board, ai_player), None

    legal = available_moves(board)

    if current_player == ai_player:
        best_val = -999
        best_move = None
        for m in legal:
            child = board[:]
            child[m] = current_player
            val, _ = minimax(child, opponent(current_player), ai_player)
            if val > best_val:
                best_val, best_move = val, m
        return best_val, best_move
    else:
        best_val = 999
        best_move = None
        for m in legal:
            child = board[:]
            child[m] = current_player
            val, _ = minimax(child, opponent(current_player), ai_player)
            if val < best_val:
                best_val, best_move = val, m
        return best_val, best_move

def best_move(ai_player="O"):
    board = get_board()
    _, move = minimax(board, ai_player, ai_player)
    return move
