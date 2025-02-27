class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    accepted_list = filter(lambda t: t.grade >= 1, attempts)
    return accepted_list

def attempts_with_grade(attempts: list, grade: int):
    return(filter(lambda t: t.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    passed_list1 = filter(lambda t: t.course_name == course, attempts)
    passed_list2 = filter(lambda t: t.grade > 0, passed_list1)
    passed_list3 = sorted(map(lambda t: t.student_name, passed_list2)) #selecting only the name and sorting in alphabetic orders
    return passed_list3


# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
# s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
# s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

# for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
#     print(attempt)