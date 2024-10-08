# Write your solution here
items = int(input("How many items: "))

i = 1
listItems = []

while i <= items:
    item = int(input(f"Items {i}: "))
    listItems.append(item)
    i += 1

print(listItems)