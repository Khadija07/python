# Write your solution here
# Write your solution here
def find_movies(database: list, search_term: str):
    d = []
    for i in range(len(database)):
        Name = database[i]['name'].lower()
        search_term = search_term.lower()
        
        if search_term in Name:
            d.append(database[i])
    
    
    return d
   
# alternative way

# movie = {"name": name,
#                "director": director,
#                "year": year,
#                "runtime": runtime}
 
#     database.append(movie)    
    
    
if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
                {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
                {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
    my_movies = find_movies(database, "python")
    print(my_movies)