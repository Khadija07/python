# Write your solution here
def invert(dictionary: dict):
    d = {}
    d = dictionary.copy()
    dictionary.clear()
    for i in d:
        value = d[i]
        dictionary[value] = i
    
    print(dictionary)
    
    

if __name__ == "__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)