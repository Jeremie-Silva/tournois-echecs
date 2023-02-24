from Models.player import Player
import json


class Controler:
    def _player_is_in_json_dataset(self, name_input, last_name_input):
        with open('Data/Players/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)
        for i in range(1,len(data_players)+1):
            if (name_input == data_players[f"player_{i}"]["name"] and
                last_name_input == data_players[f"player_{i}"]["last name"]):
                return True
        return False

    def _instance_player_from_json_dataset(self, name_input, last_name_input):
        with open('Data/Players/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        for i in range(1,len(data_players)+1):
            if (name_input == data_players[f"player_{i}"]["name"] and
                last_name_input == data_players[f"player_{i}"]["last name"]):
                birth_date_dataset = data_players[f"player_{i}"]["birth date"]
                Player(name_input, last_name_input, birth_date_dataset)
                print("ouiiiii")
            else : print("noooon")


        return


    def set_player_from_json_dataset(self):
        name_input = "efef"
        last_name_input = "efef"
        if self._player_is_in_json_dataset(name_input,last_name_input):
            self._instance_player_from_json_dataset()


Controler()._instance_player_from_json_dataset("admin","admin")