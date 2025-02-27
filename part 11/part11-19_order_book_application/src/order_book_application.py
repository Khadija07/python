# Write your solution here
# If you use the classes made in the previous exercise, copy them here

# Write your solution here:

class Task:
    count = 0
    def __init__(self, description: str, programmer: str, workload: int):
        
        self.id = Task.count + 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        Task.count += 1
        
    def is_finished(self):
        
        return self.finished
        
    
    def mark_finished(self):
        
        self.finished = True
    
    def __str__(self):
        if self.is_finished():
            return (f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED")
        return (f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED")
    
    
class PhoneBook:
    
    def __init__(self):
        self.order_list = []
        self.programmer_list = []
        
    def add_order(self):
        
        self.description = input("description: ")
        information = input("programmer and workload estimate: ")
        parts = information.split(" ")
        self.programmer = parts[0]
        if (len(parts) == 2 and parts[1].isdigit() ):
            self.workload = int(parts[1])
            print("added!")
        else:
            print('erroneous input')
            return
            
        
        
        order = Task(self.description, self.programmer,self.workload)
        self.order_list.append(order)  #all the add_orders are put in this list
        
        if self.programmer not in self.programmer_list:
            self.programmer_list.append(self.programmer)
 
        
    
    def mark_finished(self, id: int):
        if not id.isdigit():
            print("erroneous input")
            return
        for order in self.order_list:  #checking all the orders in the list, if the id matches with given id, call mark function
            #print(order.id, id)
            if int(order.id) == int(id):
                order.mark_finished()
                print("marked as finished")
                return
         
            
        print("erroneous input")
        return
                
         
                
    def finished_orders(self):
        finished_order = []
        for order in self.order_list:
            if order.is_finished() == True:
                finished_order.append(order)
                
        return finished_order
    
    def unfinished_orders(self):
        unfinished_order = []
        for order in self.order_list:
            if order.is_finished() == False:
                unfinished_order.append(order)
                
        return unfinished_order
    
    
    def status_of_programmer(self, programmer: str):
        finished_order = self.finished_orders()
        unfinished_order = self.unfinished_orders()
        count_finished = 0
        finished_time = 0
        unfinished_time = 0
        count_unfinished = 0
        
        # if programmer not in self.programmers():
        #     raise ValueError("Programmer does not exists")
        
        
        for order in finished_order:
            if order.programmer == programmer:
                count_finished += 1 
                finished_time += order.workload
            
            
        for order in unfinished_order:
            if order.programmer == programmer:
                count_unfinished += 1 
                unfinished_time += order.workload
                
        if count_finished == 0 and count_unfinished == 0:
            print('erroneous input')
            return
            # raise ValueError ("No named {programmer}")
            
        print(f"tasks: finished {count_finished} not finished {count_unfinished}, hours: done {finished_time} scheduled {unfinished_time}")
        #return (count_finished, count_unfinished, finished_time, unfinished_time)
            
        
    def all_orders(self):
        return self.order_list
    
    def programmers(self):
        return self.programmer_list
    
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
                
            elif command == "2":
                if len(self.finished_orders()) == 0:
                    print("no finished tasks")
                else:
                    for order in self.finished_orders():
                        print (f"{order.id}: {order.description} ({order.workload} hours), programmer {order.programmer} FINISHED")
            elif command == "3":
                if len(self.unfinished_orders()) == 0:
                    print("no unfinished tasks")
                else:
                    for order in self.unfinished_orders():
                        print (f"{order.id}: {order.description} ({order.workload} hours), programmer {order.programmer} NOT FINISHED")
            elif command == "4":
                id = input("id: ")
                self.mark_finished(id)
                
            elif command == "5":
                for programmer in self.programmers():
                    print(programmer)
            elif command == "6":
                p = input("programmer: ")
                self.status_of_programmer(p)
            
            # else:
            #     self.help()
    

phone = PhoneBook()
phone.execute()

# 1
# code new facebook
# jonas
# 1
# code new facebook
# jonas 10
# 3
# 0