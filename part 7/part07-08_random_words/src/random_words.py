# Write your solution here
import random 
def words(n: int, beginning: str):
    
    my_list = []
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            my_list.append(line)
        new_list = []
        i = 0
        while len(new_list) < n and i < 50000:
            
            l = random.choice(my_list)
            sum = 0
            if len(l) >= len(beginning) and l not in new_list:
                for j in range(len(beginning)):
                    if beginning[j] in l[j]:
                        sum += 1
                if sum == len(beginning):
                    new_list.append(l)
            i += 1
                    
        if len(new_list) != n:
            raise ValueError

    return new_list
   
#(5, "car"), (4, "abs"), (7, "of"), (10, "des")
# word_list = words(10, "des")
# for word in word_list:
#     print(word)


# import random
 
# def words(n: int, beginning: str):
#     word_list = []
#     with open("words.txt") as file:
#         for word in file:
#             word = word.replace("\n","")
#             if word.startswith(beginning):
#                 word_list.append(word)
#     if len(word_list) < n:
#         raise ValueError("Not enough suitable words can be found!")
#     return random.sample(word_list, n)