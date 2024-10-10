from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    my_list = []
    new_list = []
    i = 0
    length = 0
    while i < amount:    # while len(numbers) < amount:
        number = randint(lower, upper)
        #print(f"{i} n {number}")
        if number not in my_list:
            my_list.append(number)
            i += 1
        length = len(my_list)
        if length < i and i == amount-1:
            i = i - length
        
        
    my_list.sort()
    new_list = my_list.copy()
    return new_list

# for number in lottery_numbers(7, 1, 39):
#     print(number)