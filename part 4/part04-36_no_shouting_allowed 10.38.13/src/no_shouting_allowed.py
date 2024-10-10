# Write your solution here
def no_shouting(my_list: list):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i].isupper():
            continue
        new_list.append(my_list[i])
        
    return new_list

