class Item:
    def __init__(self, name: str, weight: int):
        
        self.__name = name      #names instead of name, not to confuse the name of attributes and methods
        self.__weight = weight
        
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    

class Suitcase:
    def __init__(self, max_weight: int):
        self.max = max_weight
        self.total = 0
        self.items = 0
        self.things_in_suitcase = {}
        
    def add_item(self, thing: Item):
        self.thing = thing
        
        if (self.max - self.total >= self.thing.weight()):
            self.items += 1
            self.total += self.thing.weight()
            #stored the things in suitcase in the form of dictionary
            self.things_in_suitcase[self.thing.name()] = self.thing.weight()
        #print(self.things_in_suitcase)
            
        
    def __str__(self):
        if self.items == 1:
            return f"{self.items} item ({self.total} kg)"
        return f"{self.items} items ({self.total} kg)"
    
    def print_items(self):
        #calling class Item to print 
        for key, values in self.things_in_suitcase.items():
            print(Item(key,values))
            
    def weight(self):
        return self.total
    
    def heaviest_item(self):
        max = 0
        item = ""
        for key, values in self.things_in_suitcase.items():
            #print(values)
            if values > max:
                item = key
                max = values
        
        return (Item(item,max))
    
            
        
                
            
class CargoHold:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.total_suitcase = 0
        self.prints = []
    
    def add_suitcase(self, suitcase: Suitcase):
        self.suitcase = suitcase
        #print(self.suitcase.thing)
        if self.suitcase.weight() <= self.max_weight:
            self.total_suitcase += 1
            self.max_weight -= self.suitcase.weight()
            #storing the suitcases that can be given in cargo
            self.prints.append(self.suitcase)
            
    def __str__(self):
        if self.total_suitcase == 1:
            return f"{self.total_suitcase} suitcase, space for {self.max_weight} kg"
        return f"{self.total_suitcase} suitcases, space for {self.max_weight} kg"
    
    
    def print_items(self):
        for p in self.prints:
            #calling the print_items() of class Suitcase to print
            p.print_items()
        # for item_dict in self.prints:
        #     for item, quantity in item_dict.items():  # Iterate over each dictionary
        #         print(Item(item,quantity))
    
    
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()