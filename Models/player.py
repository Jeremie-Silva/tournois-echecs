import json

class Player:
    def __init__(self, name:str, last_name:str, birth_date:int):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date

    def export_data_to_json_file(self):
        """Copy the json file in a local dictionnary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        with open('Data/Players/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        identify = len(data_players) + 1
        data_players[f'player_{identify}'] = {
            "name": self.name, 
            "last name": self.last_name,
            "birth date": self.birth_date
        }
        with open('Data/Players/players.json', 'w') as json_player_file:
            json.dump(data_players, json_player_file)
