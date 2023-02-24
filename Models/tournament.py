from Models.player import Player
import json

class Tournament:
    def __init__(self, name:str, place:str, date_start:str, date_end:str, 
                description:str, number_of_rounds:int=4):
        self.name:str = name
        self.place:str = place
        self.date_start:str = date_start
        self.date_end:str = date_end
        self.description:str = description
        self.number_of_rounds:int = number_of_rounds
        self.current_round:int = 0
        self.players_list:list[Player] = self.generate_players_list()
        self.rounds_list = self.generate_rounds_list()

    # def generate_players_list(self):
        # players_list:list[Player] = []
        # player_one = "efef"
        
        # with open('Data/Players/players.json', 'r') as json_player_file:
        #     data_players = json.load(json_player_file)

        # identify = len(data_players) + 1
        # data_players[f'player{identify}'] = {
        #     "name": self.name, 
        #     "last name": self.last_name,
        #     "birth date": self.birth_date
        # }
        # with open('Data/Players/players.json', 'w') as json_player_file:
        #     json.dump(data_players, json_player_file)
            
        # return players_list

    def _get_players(self):
        pass

    def generate_rounds_list(self):
        pass

# regional_championship = Tournament("regional championship","Toulouse","24/02/2023","25/02/2023", "Un championnat de test")
# print(regional_championship.player_one)