# Write your solution here
def everything_reversed(my_list: list):
    new_list = []
    i = len(my_list) - 1
    while i >= 0:
        new_list.append(my_list[i])
        i-=1
        
    reverse_list = []
    for item in new_list:
        line = ""
        i = len(item) - 1
        while i >= 0:
            line += item[i]
            i -= 1
        reverse_list.append(line)
    return reverse_list

# def everything_reversed(my_list: list):
#     new_list = []
#     for my_string in my_list:
#         new_list.append(my_string[::-1])
#     return new_list[::-1]