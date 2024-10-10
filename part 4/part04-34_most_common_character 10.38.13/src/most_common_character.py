# Write your solution here
def most_common_character(string: str):
    new = []
    for i in range(len(string)):
        if string[i] not in new:
            new.append(string[i])
    high = 0
    for i in range(len(new)):
        if string.count(new[i]) > high:
            high = string.count(new[i])
            letter = new[i]
            
    return letter


        