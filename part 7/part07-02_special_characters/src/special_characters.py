# Write your solution here
import string

def separate_characters(my_string: str):
    #char_list = {'.','\\','+','*', '?', '[','^',']', '$', '(', ')', '{', '}', '=', '|', ':'}
    char_list = string.punctuation
    letters = string.ascii_letters
    letters_list = []
    character = []
    others = []
    parts = []
    for i in range(len(my_string)):
        if my_string[i] in letters:
            letters_list.append(my_string[i])
        elif my_string[i] in char_list:
            character.append(my_string[i])
        else:
            others.append(my_string[i])
            
    letter = ''.join(letters_list)
    char = ''.join(character)
    other = ''.join(others)

    parts = (letter, char, other)
    return parts

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    
    
from string import ascii_letters, punctuation
 
# def separate_characters(my_string: str):
#     letters = ""
#     special_characters = ""
#     other_characters = ""
 
#     for character in my_string:
#         if character in ascii_letters:
#             letters += character
#         elif character in punctuation:
#             special_characters += character
#         else:
#             other_characters += character
 
#     return (letters, special_characters, other_characters)
    