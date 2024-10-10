# Write your solution here
def histogram(word: str):
    words = {}
    for i in range(len(word)):
        if word[i] not in words:
            words[word[i]] = 0
        words[word[i]] += 1
    
    for letter in words:
        print(letter, end = " ")
        print("*"*words[letter])
        

if __name__ == "__main__":
    histogram("abba")