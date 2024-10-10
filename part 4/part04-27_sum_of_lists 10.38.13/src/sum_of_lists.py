# Write your solution here

def list_sum(l1: list, l2: list):
    new_list = []
    for i in range(len(l1)):
        sum = l1[i] + l2[i]
        new_list.append(sum)
    return new_list

