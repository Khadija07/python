# Write your solution here
def filter_solutions():
    with open("sol1.csv") as file:
        for line in file:
            line = line.strip()
            parts = line.split(";")
            c = parts[1].split("-")
            c = parts[1].split("+")
            print(c)
filter_solutions()