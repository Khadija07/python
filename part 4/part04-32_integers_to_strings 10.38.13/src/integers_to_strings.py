# Write your solution here
def formatted(numbers: list):
    my_list = []
    for i in range(len(numbers)):
        my_list.append(f"{numbers[i]:.2f}")
    return my_list
