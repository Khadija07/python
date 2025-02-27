# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.balance = balance
        
    def deposit(self, amount: float):
        
        self.balance += amount
        self.__service_charge()
        
    def withdraw(self, amount: float):
        
        self.balance -= amount
        self.__service_charge()
        
    def __service_charge(self):
        
        charge = 0.01 * self.balance
        self.balance -= charge
        return charge
    

    def balance(self):
        return self.__service_charge()
    
    

# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100) 
# print(account.balance) #instance variables called with the name of object variables
# account.deposit(100)
# print(account.balance)
        
        


