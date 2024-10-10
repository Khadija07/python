# write your solution here
if True:
    Text = input("Write text: ")
    
with open("wordlist.txt") as file:
    #my_text = Text.lower()
    words = []
    for line in file:
        
        words.append(line.strip())
    parts = Text.split(" ")
    #words = file.read()
    text = ""
    for p in parts:
        p_lower = p.lower()
        if p_lower not in words:
            text = text + "*" + p + "*" + " "
        else:
            text = text + p + " "
    print(text)