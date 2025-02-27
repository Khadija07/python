# Write your solution here:

def order_by_season(items:list):
    return (items['seasons'])

def sort_by_seasons(items: list):
    list_items = items[:]
    list_items.sort(key=order_by_season)
    return list_items
    
# shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]
# for show in sort_by_seasons(shows):
#     print(f"{show['name']} {show['seasons']} seasons")