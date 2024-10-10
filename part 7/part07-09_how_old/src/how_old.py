# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
 
new_m = datetime(1999, 12, 31)
person = datetime(year, month, day)

if year > new_m.year:
    print("You weren't born yet on the eve of the new millennium.")
else:
    diff = new_m - person
    print(f"You were {diff.days} days old on the eve of the new millennium.")
