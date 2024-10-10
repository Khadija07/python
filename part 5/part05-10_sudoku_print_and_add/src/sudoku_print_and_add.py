# Write your solution here
def print_sudoku(sudoku: list):
    my_list = sudoku[:]
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
            
    
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku


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
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
    


