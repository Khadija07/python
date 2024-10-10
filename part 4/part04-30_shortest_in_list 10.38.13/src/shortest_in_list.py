# Write your solution here
def shortest(my_list: list):
    minimum = 99
    for i in range(len(my_list)):
        if len(my_list[i]) < minimum:
            min_string = my_list[i]
            minimum = len(my_list[i])
    return min_string

