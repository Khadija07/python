# Write your solution here
list = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    list.append(item)
    print(f"The list now: {list}")
    sortList = sorted(list)
    print(f"The list in order: {sortList}")
print("Bye!")