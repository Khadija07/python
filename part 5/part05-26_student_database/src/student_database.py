# Write your solution here
def summary(students: dict):
    print(f"students {len(students.keys())}")
    l = 0
    max_grade = 0
    for name in students:
        length = len(students[name])
        if length > l:
            l = length
            student_name = name
        grade = 0
        
        for i in range(len(students[name])):
            grade += students[name][i][1]
        avg_grade = grade/(len(students[name]))
        if max_grade < avg_grade:
            max_grade = avg_grade
            student_name_grade = name
    print(f"most courses completed {l} {student_name}")
    print(f"best average grade {max_grade} {student_name_grade}")
    
def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        l = len(students[name]) 
        if l == 0:
            print(" no completed courses")
        else:
            print(f" {l} completed courses:")
            grade = 0
            for i in range(0,l):
                print(f"  {students[name][i][0]}",end=" ")
                print(students[name][i][1])
                grade += students[name][i][1]
            
            grade = grade / (l)
            print(f" average grade {grade}")
                
    else:
        print(f"{name}: no such person in the database")
        
        
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = []

    #students[name].append(name)
    
    
    
def add_course(students: dict, name: str, course: tuple):
    if name in students:
        if course[1] == 0:
            return
        elif len(students[name]) == 0:
            students[name].append(course)
            
        else:
            for i in range(len(students[name])):
                if students[name][i][0] != course[0]:
                    students[name].append(course)
                    break
                elif students[name][i][0] == course[0]:
                    if students[name][i][1] < course[1]:
                        students[name][i] = (course[0], course[1])
                    break
                else:
                    return

if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)
