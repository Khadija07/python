def palindromes (word: str):
    w = ""
    length = len(word) - 1
    while length >= 0:
        w += word[length]
        length -= 1
    if w == word:
        return True
    else:
        return False
    

while True:
    word1 = input("Please type in a palindrome: ")
    if palindromes(word1) == True:
        print(f"{word1} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

