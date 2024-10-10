# Write your solution here
# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    open("dictionary.txt").close()
    dictionary = {}
    function = int(input("Function: "))
    if function == 1:
        with open("dictionary.txt", "a") as file:
            text_f = input("The word in Finnish: ")
            text_e = input("The word in English: ")
            file.write(f"{text_f},{text_e}\n")
            print("Dictionary entry added")
    if function == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as my_file:
            for line in my_file:
                line = line.strip()
                if search in line:
                    parts = line.split(",")
                    print(f"{parts[0]} - {parts[1]}\n")
                
            
    if function == 3:
        print("Bye!")
        break