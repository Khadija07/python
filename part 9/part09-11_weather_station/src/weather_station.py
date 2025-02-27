# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, station_name: str):
        self.__station = station_name   #private_attribute = encapsulation
        self.__observation = []
        
    def add_observation(self, observation: str):
        self.__observation.append(observation)
        
    def latest_observation(self):
        if len(self.__observation) == 0:
            
            return ""
        return self.__observation[len(self.__observation)-1]
    
    def number_of_observations(self):
        return len(self.__observation)
        
        
    def __str__(self):
        return f"{self.__station}, {len(self.__observation)} observations"
    
    


        

