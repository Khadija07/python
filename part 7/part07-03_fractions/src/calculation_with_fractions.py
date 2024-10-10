# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    my_list = []
    for i in range(amount):
        number = Fraction(1, amount)
        my_list.append(number)
    return my_list


