# tee ratkaisu tänne
# wwite your solution here

# write your solution here
if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

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
        exercise_points = int((sum/40) * 10)
        names[parts[0]].append(exercise_points)
        
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
    
    total = names[3] + names[4]
    names.append(total)
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
    g = grade(names[name])
    names[name].append(g)
# for name in names:
#     print(names[name][0], end= " ")
#     print(names[name][1], end= " ")
#     print(names[name][4], end= " ")
#     print("\n")
# print(names)
print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':10}")

# Print data
for key, values in names.items():
    name = f"{values[0]} {values[1]}"
    exec_nbr, exec_pts, exm_pts, tot_pts, grade = values[2:]
    print(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade}")


# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3