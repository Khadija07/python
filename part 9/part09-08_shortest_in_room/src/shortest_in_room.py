# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons = []
        self.total_height = 0
        self.shortest_name = None
        self.shortest_person = None
        
    def add(self, person: Person):
        self.persons.append(person)
        self.total_height += person.height
    
    def is_empty(self):
        if len(self.persons) == 0:
            return True
        return False
    
    def print_contents(self):
        height = 0
        for person in self.persons:
            height += person.height
            
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")
            
    def shortest(self):
        
        if len(self.persons) != 0:
            height = 1000000
            for person in self.persons:
                if person.height < height:
                    height = person.height
                    self.shortest_name = person
                    # print(f"{person}{self.shortest_name}")
            return self.shortest_name
        return None
    
    def remove_shortest(self):
        if len(self.persons) != 0:     
            name = self.shortest()
            self.persons.remove(name)
            return name
        
    # def remove_shortest(self):
    #     # Utilizing the previous method
    #     shortest_person = self.shortest()
    #     # equals to conditon shortest person is not None
    #     if shortest_person:
    #         self.persons.remove(shortest_person)
 
    #     return shortest_person
        

        
        
      
        

