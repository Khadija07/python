# Write your solution here
import string, random


def generate_password(amount: int):
    random_value = ""
    letters = string.ascii_lowercase
    for i in range(amount):
        random_value += random.choice(letters)
    return random_value

# for i in range(10):
#     print(generate_password(8))