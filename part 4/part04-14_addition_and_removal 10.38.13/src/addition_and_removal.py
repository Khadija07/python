# Write your solution here
list = []
print("The list is now []")
while True:
    inputItem = input("a(d)d, (r)emove or e(x)it: ")
    if(len(list) == 0):
        item = 0
    else:
        item = list[len(list)-1]
        
    if inputItem == 'x':
        break

    elif inputItem == 'd':
        list.append(item + 1)

    elif inputItem == 'r':
        list.pop(len(list)-1)

    print(f"The list is now {list}")
    

    

print("Bye!")