
def no_vowels(string: str):
    vowel = {'a','e','i','o','u'}
    line = ""
    for i in range(len(string)):
        if string[i] not in vowel:
            line += string[i]
            
            
    return line

