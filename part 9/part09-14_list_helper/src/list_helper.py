
# Class methods are usually public, so that they can be called both 
# from outside the class and from within the class, including from 
# within instances of the class. 

class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequency = {}
        for item in my_list:
            if item in frequency:
                frequency[item] += 1
                
            else:
                frequency[item] = 1
                
        
         
        max = 0       
        for key, value in frequency.items():
            if value > max:
                max = value
                most_item = key                
        return most_item
    
    @classmethod
    def doubles(cls, my_list: list):
        frequency = {}
        for item in my_list:
            if item in frequency:
                frequency[item] += 1
                
            else:
                frequency[item] = 1
                
        count = 0
        for key, values in frequency.items():
            if values >= 2:
                count += 1
                
        # doubles = 0
        # for value in counts.values(): #one other way to do it with values in tuples
        #     if value > 1:
        #         doubles += 1
 
        # return doubles
 
        
        return count
        
    
        
        

# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))
