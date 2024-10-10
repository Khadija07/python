# tee ratkaisu tänne
# Write your solution here
import math

def greatest_distance(stations: dict):
    l = len(stations)/2
    maximum = 0
    for station in stations:
        longitude1 = stations[station][0]
        latitude1 = stations[station][1]
        station1 = station
       
        for station in stations:
            if station == station1:
                continue
            longitude2 = stations[station][0]
            latitude2 = stations[station][1]
            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            
            if distance_km >= maximum:
                maximum = distance_km
                station2 = station
                station_final = station1
    return station_final, station2, maximum
                
            

def distance(stations: dict, station1: str, station2: str):
    for station in stations:
        #print(stations[station])
        #print(stations[station][0])
        if station == station1:
            longitude1 = stations[station1][0]
            latitude1 = stations[station1][1]
        if station == station2:
            longitude2 = stations[station2][0]
            latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def get_station_data(filename: str):
    dictionary = {}
    with open(filename) as file:
        for line in file:
            parts = line.split(";")
            if(parts[0] == "Longitude"):
                continue
            dictionary[parts[3]] = (float(parts[0]), float(parts[1]))
            
        return dictionary
    
    
    
if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    distance(stations, "Designmuseo", "Hietalahdentori")
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
    