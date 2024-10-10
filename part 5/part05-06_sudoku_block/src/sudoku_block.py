# Write your solution here

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

if __name__ == "__main__":
    sudoku = [
        [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
        [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
        [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
        [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
        [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
        [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
        [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
        [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
        [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
      ]
    
    print(block_correct(sudoku, 0, 0))



  