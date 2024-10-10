# Write your solution here
def line(number, symbol):
    if symbol == "":
        print(' ' * number, end = "")
    else:
        print(symbol[0]*number)

def spruce(size):
    print("a spruce!")
    i = size-1
    j = 1
    while i >= 0:
        line(i, "")
        line(j, "*")
        i -= 1
        j += 2
    line(size-1,"")
    line(1, "*")

if __name__ == "__main__":
    spruce(3)