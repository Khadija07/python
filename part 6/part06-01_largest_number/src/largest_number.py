# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        l = int(max(new_file))
        return l
        
if __name__ == "__main__":
    largest()