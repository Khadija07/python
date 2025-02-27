class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def order_by_length(items: list):
        return(items.length)

def sort_by_length(routes: list):
    list_routes = routes[:]
    list_routes.sort(key=order_by_length, reverse=True)
    
    return list_routes

# def order_by_difficulty(items: list):
#         return(items.grade)
    
def order_by_difficultyLengths(items: list):    #if the order is based on a list or a tuple, by default Python sorts the items first based on the first item, next based on the second item
    return(items.grade, items.length)
    

def sort_by_difficulty(routes: list):
    list_routes = routes[:]
    list_routes.sort(key=order_by_difficultyLengths, reverse=True)
    
    
    return list_routes


# r1 = ClimbingRoute("Small steps", 13, "6A+")
# r2 = ClimbingRoute("Edge", 38, "6A+")
# r3 = ClimbingRoute("Bukowski", 9, "6A+")
# reply = sort_by_difficulty([r1, r2, r3])
# for route in reply:
#     print(route)

# r1 = ClimbingRoute("Edge", 38, "6A+")
# r2 = ClimbingRoute("Smooth operator", 11, "7A")
# r3 = ClimbingRoute("Synchro", 14, "8C+")
# r4 = ClimbingRoute("Small steps", 12, "6A+")

# routes = [r1, r2, r3, r4]
# for route in sort_by_difficulty(routes):
#     print(route)