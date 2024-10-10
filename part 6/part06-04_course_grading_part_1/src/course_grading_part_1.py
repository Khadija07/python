# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

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
        
for name in names:
    for l in range(len(names[name])):
        print(names[name][l], end= " ")
    print("\n")
                    