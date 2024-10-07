def line(number, symbol):
    if symbol == "":
        print('*' * number)
    else:
        print(symbol[0]*number)

def shape(size, char, size1, char1):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, char)
        i += 1
    i = 1
    while i <= size1:
        line(size, char1)
        i += 1
        
if __name__ == "__main__":
    shape(5, "x", 2, "o")