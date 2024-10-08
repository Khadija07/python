# Write your solution here
# You can test your function by calling it within the following block
def length(listItems: list):
    lengthList = len(listItems)
    return lengthList
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(f"The length is {result}")