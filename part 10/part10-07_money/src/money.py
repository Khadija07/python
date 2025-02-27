# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        return f"{self.__euros}.{self.__cents} eur"
    
    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents
        
    def __lt__(self, another):
        return self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents)
    
    def __gt__(self, another):
        return self.__euros > another.__euros or (self.__euros == another.__euros and self.__cents > another.__cents)
    
    def __add__(self, another):
        sum_euros = 0
        sum_cents = self.__cents + another.__cents
        if sum_cents == 100:
            sum_euros += 1
            sum_cents = 0
        sum_euros = (sum_euros + self.__euros + another.__euros) * 100
        total = (sum_euros + sum_cents)/100
        return f"{total:.2f} eur" 
    
    def __sub__(self, another):
        
        if self.__cents < another.__cents and self.__euros > another.__euros:
            self.__cents = self.__cents + 100
            self.__euros = self.__euros - 1
            
            
        sum_euros = self.__euros - another.__euros
        sum_cents = self.__cents - another.__cents
        
        if sum_euros < 0 or sum_cents < 0:
            raise ValueError(f"a negative result is not allowed")
        total = ((sum_euros*100) + sum_cents) / 100
        return f"{total:.2f} eur"
    
# e1 = Money(4, 5)
# e2 = Money(2, 95)


# e3 = e1 + e2
# e4 = e1 - e2

# print(e4)
# print(e3)

# e5 = e2-e1
        
        
