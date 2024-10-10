# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 <= x <= 2 and 0 <= y <= 2:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False
    else:
        return False
    
# game_board = [['X', 'O', ''], ['O', 'O', 'O'], ['', '', '']]
# print(play_turn(game_board, 3, 0, "X"))
# print(game_board)