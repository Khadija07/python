# Write your solution here
def oldest_person(people: list):
    year = 100000000000
    for p in people:
        if p[1] < year:
            year = p[1]
    for p in people:
        if p[1] == year:
            name = p[0]
            break
    return name
            
        

