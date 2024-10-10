# Write your solution here
def row_correct(sudoku: list, row_no: int):
    s_list = []
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] not in s_list or sudoku[row_no][i] == 0:
            s_list.append(sudoku[row_no][i])
            
    if len(sudoku) == len(s_list):
        return True
    else:
        return False
        

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(row_correct(sudoku, 1))



  