# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    total1 = (person1['result1'] + person1['result2'] + person1['result3'])/3
    total2 = (person2['result1'] + person2['result2'] + person2['result3'])/3
    total3 = (person3['result1'] + person3['result2'] + person3['result3'])/3
    
    if total1 < total2 and total1 < total3:
        return person1
    if total2 < total1 and total2 < total3:
        return person2
    else:
        return person3
    


    