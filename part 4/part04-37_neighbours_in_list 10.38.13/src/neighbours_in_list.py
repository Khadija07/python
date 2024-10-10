# Write your solution here

def longest_series_of_neighbours(my_list: list):
    total = 0
    count = 1
    for i in range(len(my_list)):
        if abs(my_list[i] - my_list[i-1]) == 1:
            count += 1
        else:
            total = max(total, count)
            count = 1
    total = max(total, count)
    return total

# my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
# print(longest_series_of_neighbours(my_list))
        