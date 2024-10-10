# Write your solution here
import math

def hypotenuse(leg1: float, leg2: float):
    add = (leg1 * leg1) + (leg2 * leg2)   #return sqrt(leg1 ** 2 + leg2 ** 2)
    result = math.sqrt(add)
    return result
