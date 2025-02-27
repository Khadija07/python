# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __eq__(self, another):
        return self.day == another.day and self.month == another.month and self.year==another.year
    
    def __ne__(self, another):
        return self.day != another.day  or self.month != another.month or self.year != another.year
        
    def __lt__(self, another):
                    
        return self.year < another.year or (self.month < another.month and self.year == another.year) or ( self.day < another.day and self.month == another.month and self.year == another.year)
    
    def __gt__(self, another):
                    
        return self.year > another.year or (self.month > another.month and self.year == another.year) or ( self.day > another.day and self.month == another.month and self.year == another.year)
    
    
    def __add__(self, days):
        
        day = self.day
        month = self.month
        year = self.year
        
        while(days > 0):
            days_left = 30 - day
            
            if days <= days_left:
                day += days
                days = 0
                
            else:
                
                days = days - (days_left + 1) ## subtracting the remaining days in the month and begin the next month
                day = 1 #first date of next month
                
                if month != 12:
                    month += 1
                    
                else:
                    month = 1
                    year += 1
                    
        return SimpleDate(day, month, year)
    
    def __sub__(self, another):
        
        year = abs(self.year - another.year)
        month = abs(self.month - another.month)
        day = abs(self.day - another.day)
        
        if (self.year > another.year):
            result = abs((year * 360) - ((month * 30) + (day)))
        
        else:
            
            result = abs((year * 360) + ((month * 30) + (day)))
        
        return result
                
                
# sd1 = SimpleDate(1, 4, 1800)
# sd2 = SimpleDate(3, 5, 1842)

# print(sd1-sd2)
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(2, 11, 2020)
# d3 = SimpleDate(28, 12, 1985)

# print(d2-d1)
# print(d1-d2)
# print(d1-d3)
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)

# d3 = d1 + 3
# d4 = d2 + 400

# print(d1)
# print(d2)
# print(d3)
# print(d4)
    
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
# d3 = SimpleDate(28, 12, 1985)
# sd1 = SimpleDate(1, 7, 1999)
# sd2 = SimpleDate(1, 8, 1999)

# print(sd1 != sd2)
# print(d1)
# print(d2)
# print(d1 == d2)
# print(d1 != d2)
# print(d1 == d3)
# print(d1 < d2)
# print(d1 > d2)       
   