dictionary = {}
while True:
    #print("command (1 search, 2 add, 3 quit): ", end="")
    order = int(input())
    
    if order == 1:
        name = input("name: ")
        if name in dictionary:
            print(dictionary[name])
        else:
            print("no number")
                
    if order == 2:
        name = input("name: ")
        number = input("number: ")
        dictionary[name] = number
        print("ok!")
        
    if order == 3:
        print("quitting...")
        break

        

        
        
        