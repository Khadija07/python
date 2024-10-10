# Write your solution here
number = int(input("Please type in a positive integer: "))
n = number - (number * 2)


for i in range(n,number):
    if i == 0:
        continue
    print(i)

print(number)
