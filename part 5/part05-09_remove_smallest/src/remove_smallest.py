# Write your solution here
def remove_smallest(numbers: list):
    my_list = numbers[:]
    my_list.sort()
    smallest = my_list[0]
    for i in numbers:
        if i == smallest:
            numbers.remove(i)
            

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)