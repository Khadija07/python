# Write your solution here:
import random

def word_generator(characters: str, length: int, amount: int):
    word_list = []
    if length > len(characters):
        raise ValueError("length bigger than word length")
    
    for i in range(0, amount):
        start = random.randint(0, len(characters) - length)
       
        yield(characters[start:start+length])
        
    

# wordgen = word_generator("abc",2,1)
# for word in wordgen:
#     print(word)

# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))
 