# Write your solution here

def length_of_longest(my_list: list):
    highest = 0
    for i in range(len(my_list)):
        if len(my_list[i]) >= highest:
            highest = len(my_list[i])
    return highest


