# WRITE YOUR SOLUTION HERE:
import string

def most_common_words(filename: str, lower_limit: int):
    book = open(filename,'r').read()
    book =''.join([char for char in book if char not in string.punctuation])

    word = {}
    for b in book.split():
        if b in word:
            
            word[b] += 1
        else:
            word[b] = 1
            
    
    return {key: value for key,value in word.items() if value >= lower_limit}
        
    

# print(most_common_words("comprehensions.txt", 4))