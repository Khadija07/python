def line(number, symbol):
    if symbol == "":
        print('*' * number)
    else:
        print(symbol[0]*number)

def square(size, character):
    # You should call function line here with proper parameters
    height = size
    while height > 0:
        line(size, character)
        height -= 1

    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "o")