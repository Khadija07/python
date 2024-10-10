# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        with open("diary.txt", "a") as file:
            text = input("Diary entry: ")
            file.write(f"{text}\n")
            print("Diary saved")
            print()
    if function == 2:
        print("Entries:")
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line) 
    if function == 0:
        print("Bye now!")
        break