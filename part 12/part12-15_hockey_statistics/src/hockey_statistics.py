# Write your solution here
import json
class Players:
    def __init__(self):
        self.team_lists = []
        self.country_lists = []
        
        
    
    def search_player(self, name: str):
        for player in self.players_data:
            if player['name'] == name:
                total = player['goals'] + player['assists']
                print(f"{player['name']:<20} {player['team']:<5}{player['goals']:2} + {player['assists']:2} = {total:3}")
    
    def teams(self):
        for player in self.players_data:
            self.team_lists.append(player['team'])
            
        self.team_lists = sorted(set(self.team_lists))
        for team in self.team_lists:
            print(team)
    def countries(self):
        for player in self.players_data:
            self.country_lists.append(player['nationality'])
            
        self.country_lists = sorted(set(self.country_lists))
        for country in self.country_lists:
            print(country)
    
    def players_in_team(self, team: str):
        total_score = []
        for player in self.players_data:
            if player['team'] == team:
                total = player['goals'] + player['assists']
                total_score.append((player['name'],total))
        sorted_score = sorted(total_score, key=lambda x: x[1], reverse=True)
        for s in sorted_score:
            self.search_player(s[0])
        
    def players_in_country(self, country: str):
        total_score = []
        for player in self.players_data:
            if player['nationality'] == country:
                total = player['goals'] + player['assists']
                total_score.append((player['name'],total))
        sorted_score = sorted(total_score, key=lambda x: x[1], reverse=True)
        for s in sorted_score:
            self.search_player(s[0])
                
        
        
    def help(self):
        
        print("\n")
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.filename = input("file name: ")
        with open(self.filename) as my_file:
            data = my_file.read()

        self.players_data = json.loads(data)
        length = len(self.players_data)
        #print(f"file name: {self.filename}")
        print(f"read the data of {length} players")
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                self.search_player(name)
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                name = input("team: ")
                self.players_in_team(name)
            elif command == "5":
                name = input("country: ")
                self.players_in_country(name)
                
            
            

player = Players()
player.execute()