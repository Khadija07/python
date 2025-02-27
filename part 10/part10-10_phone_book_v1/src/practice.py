class PhoneBook:
    def __init__(self):
        self.__persons = {}
        
    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            self.__persons[name] = []

        self.__persons[name].append(number) #add all the numbers under the name

    def get_numbers(self, name: str):
        if name,number in self.__persons.values():
            print (self.__persons[name])
        
    
p = PhoneBook()
p.add_number('eric','789')
p.add_number('iu','567')
p.get_numbers('567')
    
# class PhoneBookApplication:
#     def __init__(self):
#         self.__phonebook = PhoneBook()
        

#     def help(self): #prints out the commands
#         print("commands: ")
#         print("0 exit")
#         print("1 add entry")
#         print("2 search")

#     def add_entry(self):
#         name = input("name: ")
#         number = input("number: ")
#         self.__phonebook.add_number(name, number)

#     def search(self):
#         name = input("name: ")
#         numbers = self.__phonebook.get_numbers(name)
#         if numbers == None:
#             print("number unknown")
#             return
#         for number in numbers:
#             print(number)

#     def execute(self):
#         self.help()
#         while True:
#             print("")
#             command = input("command: ")
#             if command == "0":
#                 break
#             elif command == "1":
#                 self.add_entry()
#             elif command == "2":
#                 self.search()
#             else:
#                 self.help()
                
# class FileHandler():
#     def __init__(self, filename):
#         self.__filename = filename

#     def load_file(self):
#         names = {}
#         with open(self.__filename) as f:
#             for line in f:
#                 parts = line.strip().split(';')
#                 name, *numbers = parts # the * in front of the variable means it can contain all the remaining items of the list
#                 names[name] = numbers

#         return names
    
    
# # code for testing

# application = PhoneBookApplication()
# application.execute()

# # phonebook = PhoneBook()
# # phonebook.add_number("Eric", "02-123456")
# # phonebook.add_number("Eric", "02-123477")
# # print(phonebook.get_numbers("Eric"))
# # print(phonebook.get_numbers("Emily"))
    