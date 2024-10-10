# Write your solution here

def distinct_numbers(my_list: list):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    sort_list = sorted(new_list)
    return sort_list

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]