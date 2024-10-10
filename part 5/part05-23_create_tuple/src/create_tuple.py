# Write your solution here

def create_tuple(x: int, y: int, z: int):
    number = ()
    if x < y and x < z:
        smallest = x
    if y < x and y < z:
        smallest = y
    if z < x and z < y:
        smallest = z
    if x > y and x > z:
        largest = x
    if y > x and y > z:
        largest = y
    if z > x and z > y:
        largest = z
        
    
    sum = x + y + z
    number = (smallest, largest, sum)
    
    return number 
        
    
    
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
    


# def create_tuple(x: int, y: int, z: int):
#     """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
#     smallest = min([x, y, z])
#     greatest = max([x, y, z])
#     sum = x + y + z # sum([x, y, z]) also works
 
#     return (smallest, greatest, sum)