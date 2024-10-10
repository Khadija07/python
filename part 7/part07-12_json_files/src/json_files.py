# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    persons = json.loads(data)
    
    for person in persons:
        hobbies = ', '.join(person["hobbies"])
        print(f"{person['name']} {person['age']} years ({hobbies})")
        
# print_persons('file1.json')