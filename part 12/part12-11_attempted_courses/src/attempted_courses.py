class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
    

# Write your solution here
def names_of_students(attempts: list):
    students_names = map(lambda t: t.student_name, attempts) #works like a list, but map is an iterator; passing through it with a for loop "depletes" it, 
    # much like a generator is depleted once its maximum value is reached. 
    return (students_names)
    
def course_names(attempts: list):
    courses = map(lambda t: t.course_name, attempts)
    courses_sorted = set(sorted(courses, key=lambda word: word[0])) # remove duplicates by using a set
    return courses_sorted

# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
# s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

# for name in course_names([s1, s2, s3]):
#     print(name)