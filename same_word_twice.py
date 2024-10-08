# Write your solution here
list = []
count = 0

while True:
    word = input("Word: ")
    if word in list:
        break
    list.append(word)
    count += 1

print(f"You typed in {count} different words")
