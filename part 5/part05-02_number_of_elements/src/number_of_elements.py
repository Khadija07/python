# Write your solution here

def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for i in range(len(my_matrix)): # using the number of rows in the matrix
        for j in range(len(my_matrix[i])): # using the number of items on each row 
            if my_matrix[i][j] == element:
                count += 1

    return count
        
    
if __name__ == "__main__":
    
    print(count_matching_elements([[1, 2]], 1))



