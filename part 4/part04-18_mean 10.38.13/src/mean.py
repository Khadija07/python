# Write your solution here
# You can test your function by calling it within the following block
import math

def mean(List: list):
    total = sum(List)
    mean = total / len(List)
    return mean

if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = mean(my_list)
    print(f"mean value is {result}")