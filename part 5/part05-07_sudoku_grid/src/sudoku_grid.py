
def row_correct(sudoku: list, row_no: int):
    s_list = []
    for i in range(len(sudoku[row_no])):
        if sudoku[row_no][i] not in s_list or sudoku[row_no][i] == 0:
            s_list.append(sudoku[row_no][i])
            
    if len(sudoku) == len(s_list):
        return True
    else:
        return False
        

def column_correct(sudoku: list, column_no: int):
    s_list = []
    for i in range(len(sudoku[column_no])):
        if sudoku[i][column_no] in s_list and sudoku[i][column_no] != 0:
            return False
        else:
            s_list.append(sudoku[i][column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    s_list = []
    row = row_no
    for i in range(3):
        for j in range(3):
            if sudoku[row_no + i][column_no + j] in s_list and sudoku[row_no + i][column_no + j] != 0:
                return False
                break
            else:
                s_list.append(sudoku[row_no + i][column_no + j])
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        row_check = row_correct(sudoku, i)
        column_check = column_correct(sudoku, i)
        if i%3 == 0:
            j = i
            k = 0
            block_check = block_correct(sudoku, j, k)
        else:
            k += 3
            block_check = block_correct(sudoku, j, k)
        
        if row_check == True and column_check == True and block_check == True:
            continue
        else:
            return False
            break
    return True
    
  
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
    print(sudoku_grid_correct(sudoku))



  