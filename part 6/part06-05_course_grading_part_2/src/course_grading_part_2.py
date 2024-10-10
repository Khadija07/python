# wwite your solution here

# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")

with open(student_info) as students:
    names = {}
    for line in students:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = []
        names[parts[0]].append(parts[1].strip())
        names[parts[0]].append(parts[2].strip())   #students[parts[0]] = f"{parts[1]} {parts[2].strip()}"

with open(exercise_data) as file:
    exercise = {}
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        #print(type(parts[1]))
        e1 = int(parts[1])
        e2 = int(parts[2])
        e3 = int(parts[3])
        e4 = int(parts[4])
        e5 = int(parts[5])
        e6 = int(parts[6])
        e7 = int(parts[7])
        sum = e1+ e2 +e3 + e4 + e5 + e6 + e7
        names[parts[0]].append(sum)
        
with open(exam_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for i in range(1,4):
            sum += int(parts[i])
        names[parts[0]].append(sum)

def grade(names: list):
    exercise_points = int((names[2]/40) * 10)
    total = exercise_points + names[3]
    if total >= 0 and total <= 14:
        return 0
    elif total >= 15 and total <= 17:
        return 1
    elif total >= 18 and total <= 20:
        return 2
    elif total >= 21 and total <= 23:
        return 3
    elif total >= 24 and total <= 27:
        return 4
    else:
        return 5
        
for name in names:
    total = names[name][2] + names[name][3]
    g = grade(names[name])
    names[name].append(g)

for name in names:
    print(names[name][0], end= " ")
    print(names[name][1], end= " ")
    print(names[name][4], end= " ")
    print("\n")
                   