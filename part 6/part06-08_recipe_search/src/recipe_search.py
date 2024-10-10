# Write your solution here
def search_by_ingredient(filename: str, ingredient: str):
    my_list = []
    time_list = []
    with open(filename) as file:
        for line in file:
            my_list.append(line.strip())
        print(my_list)
        
    
def search_by_time(filename: str, prep_time: int):
    my_list = []
    time_list = []
    with open(filename) as file:
        for line in file:
            my_list.append(line.strip())
        for i in range(len(my_list)):
            if i == 1 or my_list[i-2] == '':
                if int(my_list[i]) <= prep_time:
                    time_list.append(f"{my_list[i-1]}, preparation time {my_list[i]} min")
        #print(time_list)
        return time_list
    
    
    
    
def search_by_name(filename: str, word: str):
    recipe_list = []
    my_list = []
    with open(filename) as file:
        for line in file:
            my_list.append(line.strip())
        #print(my_list)
        for i in range(len(my_list)):
          
            if i == 0 or my_list[i-1] == '':
                if word.lower() in my_list[i].lower():
                    recipe_list.append(my_list[i])
        return recipe_list
        
    
    
    
if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    # for recipe in found_recipes:
    #     print(recipe)
