
# Write your solution here:
class Person:
    
    def __init__(self, name:str):
        self.__name = name
        self.__number = []
        self.__address = None
        # if name not in self.__persons:
        #     self.__persons[self.__name] = {'number': [], 'address': None} #assign two values under one key in dictionary

    def add_number(self, number: str):
        self.__number.append(number)
            
        #self.__persons[self.__name]['number'].append(number)
        
    def add_address(self, address: str):
        self.__address = address
        #self.__persons[self.__name]['address'] = address
        
    def name(self):
        return self.__name
        
    def numbers(self):
        return self.__number
    
    def address(self):
        return self.__address
    
class PhoneBook:
    def __init__(self):
        
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
        
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)  #create object of class Person,objects of class Person to store value in dictionary.
        self.__persons[name].add_address(address)
    
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()
    
    def get_address(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()
    
    
    def all_entries(self):
        return self.__persons
    

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
        
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
        

    def search(self):
        name = input("name: ")
            
        
        address = self.__phonebook.get_address(name)
        numbers = self.__phonebook.get_entry(name)
        if numbers is None and address is None:
            print(f"address unknown")
            print("number unknown")
        elif numbers is None:
            print("number unknown")
        elif numbers == [] and address is not None:
            print("number unknown")
            print(address)
        else:
            print(f"{numbers}")
            if address:
                print(f"{address}")
            else:
                print("address unknown")
            
                 
            
              

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
                



# when testing, no code should be outside application except the following:

application = PhoneBookApplication()
application.execute()

# 3
# Erkki
# Linnankatu 10
# 2
# Erkki
# 0

# 09-123456
# with input
# 1
# Emilia
# 09-123456
# 1
# Emilia
# 040-999999
# 2
# Emilia
# 0

# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())