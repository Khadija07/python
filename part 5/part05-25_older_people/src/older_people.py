# Write your solution here
def older_people(people: list, year: int):
    older = []
    for p in people:
        if p[1] < year:
            older.append(p[0])
            
    return older
        