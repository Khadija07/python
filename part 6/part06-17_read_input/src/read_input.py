# Write your solution here

def read_input(text: str, lower: int, higher: int):
    while True:
        try:
            number = input(text)
            if number.isdigit():
                if lower <= int(number) <= higher:
                    return int(number)
                
        except ValueError:
            pass
        print(f"You must type in an integer between {lower} and {higher}")
        
    # number = input(text)
    # if number.isdigit():
    #     if lower <= int(number) <= higher:
    #         return number
    #     else:
    #         print(f"You must type in an integer between {lower} and {higher}")
    #         number = read_input("Please type in a number: ", lower, higher)
    # else:
    #     print(f"You must type in an integer between {lower} and {higher}")
    #     number = read_input("Please type in a number: ", lower, higher)
    

