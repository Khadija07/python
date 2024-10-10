# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] > 0:
            sum += my_list[i]
        
    return sum

# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)
