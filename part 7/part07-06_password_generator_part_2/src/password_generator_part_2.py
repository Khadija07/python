# Write your solution here
# Write your solution here
import string, random


def generate_strong_password(amount: int, arg1: bool, arg2: bool):
    random_value = ""
    letters = string.ascii_lowercase
    char_list = {'!', '?', '=', '+', '-', '(', ')', '#'}
    while len(random_value) < amount :
        #print(f"l {len(random_value)}")
        random_value += random.choice(letters)
        if arg1 == True and len(random_value) < amount:
            random_value += str(random.randint(1,9))
        if arg2 == True and len(random_value) < amount:
            random_value += str(random.choice(list(char_list)))
            #print(f"l {len(random_value)} {random_value}")
    return random_value


# for i in range(10):
#     print(generate_strong_password(5, False, True))