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
    
class OrderBook:
    
    
    def __init__(self):
        self.order_list = []
        self.programmer_list = []
        
    def add_order(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        
        order = Task(self.description, self.programmer,self.workload)
        self.order_list.append(order)  #all the add_orders are put in this list
        #self.marked_list[self.order] = OrderBook.counts
        
        if self.programmer not in self.programmer_list:
            self.programmer_list.append(self.programmer)
            
            
    def mark_finished(self, id: int):
        
        for order in self.order_list:  #checking all the orders in the list, if the id matches with given id, call mark function
            if order.id == id:
                order.mark_finished()
                return
            
        raise ValueError("order {id} not found") #if id not fount
                
        
        # for key, value in self.marked_list.items():
            
            
        #     if value == id:
        #         self.order.mark_finished()
        #         print(id,self.order.is_finished())
        #         return
        #raise ValueError
            
         
                
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
            raise ValueError ("No named {programmer}")
            
        return (count_finished, count_unfinished, finished_time, unfinished_time)
            
        
    def all_orders(self):
        return self.order_list
    
    def programmers(self):
        return self.programmer_list
    

# orders = OrderBook()
# orders.add_order("program webstore", "Adele", 10)
# orders.add_order("program mobile app for workload accounting", "Adele", 25)
# orders.add_order("program app for practising mathematics", "Adele", 100)
# orders.add_order("program the next facebook", "Eric", 1000)

# orders.mark_finished(1)
# orders.mark_finished(2)

# status = orders.status_of_programmer("Adele")
# print(status)


