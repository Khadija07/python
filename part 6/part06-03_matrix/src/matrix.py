# write your solution here
def matrix_sum():
    with open("matrix.txt") as file:
        sum = 0
        for line in file:
            line = line.split(",")
            for l in range(len(line)):
                sum += int(line[l])
                
        return sum
        
def matrix_max():
    with open("matrix.txt") as file:
        my_list = []
        for line in file:
            line = line.split(",")
            
            for l in range(len(line)):
                my_list.append(int(line[l]))
        maximum = max(my_list)
        return maximum
        
def row_sums():
    with open("matrix.txt") as file:
        my_list = []
        for line in file:
            line = line.split(",")
            sum = 0
            for l in range(len(line)):
                sum += int(line[l])
            my_list.append(sum)
            
        return my_list
            
            
if __name__ == "__main__":
    print(matrix_max())