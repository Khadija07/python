# tee ratkaisusi tänne
class CourseRecordApplication:
    def __init__(self):
        self.__courserecord = {}

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        
    def get_grade(self, course: str):
        for key, value in self.__courserecord.items():
            if key == course:
                #print(value), max of all the grades
                return(max(value['grades'])) 
        
        
        
    def get_credits(self, course: str):
        for key, value in self.__courserecord.items():
            if key == course:
                #max of all credits
                return(max(value['credits']))
       

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        if course not in self.__courserecord:
            # initialize for new grades and credits
            self.__courserecord[course] = {'grades': [], 'credits': []}
        
        # Append in the lists 
        self.__courserecord[course]['grades'].append(grade)
        self.__courserecord[course]['credits'].append(credits)
        # self.__courserecord[course] = {'grade' : grade, 'credit' : credits}
        
            
    def get_course_data(self):
        course = input("course: ")   
        grade = self.get_grade(course)
        credits = self.get_credits(course)
        if grade is None and credits is None:
            print(f"no entry for this course")
        else:
            print(f"{course} ({credits} cr) grade {grade}")

            
    def statistics(self):
        
        count_grades = 0
        count_credits = 0
        completed_courses = len(self.__courserecord)
        grade_list = []
        
        for course in self.__courserecord:
            #total grades and credits
            count_grades += self.get_grade(course)
            count_credits += self.get_credits(course)
            
            #putting all the grades in a list for grade distribution
            grade_list.append(self.get_grade(course))
            
        #mean value
        mean = count_grades/completed_courses
        print(f"{completed_courses} completed courses, a total of {count_credits} credits")
        print(f"mean {mean:.1f}")
        
        grade_list.sort(reverse=True)
        #print(grade_list)
        print("grade distribution")
        
        #counting the total of each grade, if not in grade_list, it is assigned 0
        count_grade = {}
        if 1 not in grade_list:
            count_grade[1] = 0
        if 2 not in grade_list:
            count_grade[2] = 0
        if 3 not in grade_list:
            count_grade[3] = 0
        if 4 not in grade_list:
            count_grade[4] = 0
        if 5 not in grade_list:
            count_grade[5] = 0
            
        for grade in grade_list:
            if grade in count_grade:
                count_grade[grade] += 1
            else:
                count_grade[grade] = 1
            
        for key, values in count_grade.items():
            print(f"{key}: {values*'x'}")
            
            

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

# when you run the tests, nothing apart from these two lines should be placed in the main function, outside any class definitions 
application = CourseRecordApplication()
application.execute()
