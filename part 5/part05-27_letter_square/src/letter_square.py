# Write your solution here
def square_of_letters(layers):
    List_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
                        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                        'U', 'V', 'W', 'X', 'Y', 'Z']
    result = []
    for i in range(layers):
    # updating existing rows
        for j, pattern in enumerate(result):
            result[j] = List_of_letters[i] + pattern + List_of_letters[i]
            #print(pattern, result)
            

    # adding top and bottom row
        result.append((i*2 + 1)*List_of_letters[i])
        if i != 0:
            result.insert(0, (i*2 + 1)*List_of_letters[i])
    
    for res in result:
        print(res)


n = int(input("Layers: "))
square_of_letters(n)
