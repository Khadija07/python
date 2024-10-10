import copy
def print_sudoku(sudoku: list):
    for i in range(9):
        if(i%3 == 0 and i != 0):
            print()
            print()
        else:
            print()
        for j in range(9):
            if((j+1)%3==0):
                if sudoku[i][j] == 0:
                    print("_", end="  ")
                else:
                    print(sudoku[i][j], end="  ")
                                
            else:
                if sudoku[i][j] == 0:
                    print("_", end=" ")
                else:
                    print(sudoku[i][j], end=" ")
                    
    print()
            
    
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
    new_list[row_no][column_no] = number
    
    return new_list


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
   
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
    


