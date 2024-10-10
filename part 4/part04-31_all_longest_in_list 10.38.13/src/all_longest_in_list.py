# Write your solution here
def all_the_longest(my_list: list):
    minimum = 0
    min_string = []
    for i in range(len(my_list)):
        if len(my_list[i]) > minimum:
            string = my_list[i]
            minimum = len(my_list[i])
    min_string.append(string)
    for i in range(len(my_list)):
        if len(my_list[i]) == minimum and my_list[i] not in min_string:
            min_string.append(my_list[i])

    return min_string

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']