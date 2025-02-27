# TEE RATKAISUSI TÄHÄN:
def order_by_season(items:list):
    return (items['rating'])

def sort_by_ratings(items: list):
    list_items = items[:]
    list_items.sort(key=order_by_season, reverse=True)
    return list_items

# shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

# print("Rating according to IMDB")
# for show in sort_by_ratings(shows):
#     print(f"{show['name']}  {show['rating']}")
    