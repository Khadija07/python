# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, width: int):
        super().__init__(width, height= None)   #to use one attribute from base class, simply ignore the other attribute when initializing the subclass
        # def __init__(self, side: int):
        # # Provide the side as width and height for the
        # # superclass constructor
        # super().__init__(side, side)
        
    def area(self):
        return self.width * self.width
    
    def __str__(self):
        return f"square {self.width}x{self.width}"
    
# square = Square(4)
# print(square)
# print("area:", square.area())