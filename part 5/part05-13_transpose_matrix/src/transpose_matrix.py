# Write your solution here
def print_transpose(matrix:list):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=" ")
            
        print()
    
def transpose(matrix: list):
    new_list = []
    for r in matrix:      //copying List
        new_list.append(r[:])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_list[i][j]= matrix[j][i]
            
    for i in range(len(matrix)):
        matrix[i] = new_list[i]   #copying one by one in List

    print_transpose(matrix)
            
            
if __name__ == "__main__":
    matrix = [[1,2], [1,2]]
    transpose(matrix)
