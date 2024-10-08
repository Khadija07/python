# Write your solution here
def even_numbers(my_list: list):
    new_list = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            new_list.append(my_list[i])
    return new_list
