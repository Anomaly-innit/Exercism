def gamestate(board):
   
    xs = sum(row.count("X") for row in board)
    os = sum(row.count("O") for row in board)
    if os > xs:
        raise ValueError("Wrong turn order: O started")
    elif xs > os+1:
        raise ValueError("Wrong turn order: X went twice")
    if wins(board, "X") and wins(board, "O"):
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif wins(board, "X") or wins(board, "O"):
        return "win"
    elif " " not in board[0] + board[1] + board[2]:
        return "draw"
    else:
        return "ongoing"
        
def wins(board, player):
    return (
        board[0][0] == board[0][1] == board[0][2] == player or
        board[1][0] == board[1][1] == board[1][2] == player or
        board[2][0] == board[2][1] == board[2][2] == player or
        board[0][0] == board[1][0] == board[2][0] == player or
        board[0][1] == board[1][1] == board[2][1] == player or
        board[0][2] == board[1][2] == board[2][2] == player or
        board[0][0] == board[1][1] == board[2][2] == player or
        board[0][2] == board[1][1] == board[2][0] == player
    )