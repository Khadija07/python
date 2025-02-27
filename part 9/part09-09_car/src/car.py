# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__distance = 0
        
    def fill_up(self):
        self.__petrol = 60
        
        
    def drive(self, km:int):
        
        petrol_needed = km 
        if petrol_needed <= self.__petrol:
            self.__petrol -= petrol_needed
            self.__distance += km
        else:
            self.__distance += self.__petrol
            self.__petrol = 0
            
            
    def __str__(self):
        return f"Car: odometer reading {self.__distance} km, petrol remaining {self.__petrol} litres"
        

# car = Car()
# print(car)
# car.fill_up()
# print(car)
# car.drive(20)
# print(car)
# car.drive(50)
# print(car)
# car.drive(10)
# print(car)
# car.fill_up()
# car.fill_up()
# print(car)
            
            
    

