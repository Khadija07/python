# write your solution here
def read_fruits():
    dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            dictionary[parts[0]] = float(parts[1])
    return dictionary
            
            
            
if __name__ == "__main__":
    read_fruits()