# Write your solution here
def who_won(game_board: list):
    count_zero = 0
    count_one = 0
    count_two = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                count_one += 1
            elif game_board[i][j] == 2:
                count_two += 1

    if(count_one > count_two):
        return 1
    elif(count_one < count_two):
        return 2
    elif(count_one == count_two):
        return 0

if __name__ == "__main__":
    print(who_won([[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]))