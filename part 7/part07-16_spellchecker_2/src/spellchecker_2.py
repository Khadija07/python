# Write your solution here
# write your solution here
from difflib import get_close_matches

if True:
    Text = input("Write text: ")
    
with open("wordlist.txt") as file:
    #my_text = Text.lower()
    words = []
    suggestions = {}
    for line in file:
        
        words.append(line.strip())
    parts = Text.split(" ")
    #words = file.read()
    text = ""
    wrong = []
    for p in parts:
        p_lower = p.lower()
        suggestions[p] = get_close_matches(p, words, n=3)
        if p_lower not in words:
            text = text + "*" + p + "*" + " "
            wrong.append(p)
        else:
            text = text + p + " "
    print(text)
    print("suggestions:")
    for key, value in suggestions.items():
        print(f"{key}: {', '.join(value)}")
        
    
    