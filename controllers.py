import json
import datetime
from typing import Literal
from models import Player


class DataController:
    def get_information_user(self, message: str, data_type: Literal["string", "day_date", "integer"] = "string"):
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        input_year: str = ""
        input_month: str = ""
        input_day: str = ""
        while True:
            if data_type == "string":
                try:
                    input_value = str(input(f"{message} : "))
                    if input_value.isalpha() and len(input_value) < 100:
                        break
                except ValueError:
                    pass
            elif data_type == "day_date":
                print(f"{message} : ")
                try:
                    input_year = str(input("Année : "))
                    input_month = str(input("Mois : "))
                    input_day = str(input("Jour : "))
                    if (input_year.isdigit() and len(input_year) == 4 and
                        input_month.isdigit() and len(input_month) == 2 and int(input_month) <= 12 and
                        input_day.isdigit() and len(input_day) == 2 and int(input_day) <= 31
                    ):
                        input_value = str(datetime.date(int(input_year), int(input_month), int(input_day)))
                        break
                except ValueError:
                    pass
            elif data_type == "integer":
                try:
                    input_value = int(input(f"{message} : "))
                    if (str(input_value).isdigit() and
                            len(str(input_value)) == 1 or len(str(input_value)) == 2
                    ):
                        break
                except ValueError:
                    pass
            else:
                raise ValueError
            print(f"-Erreur- {message} invalide")
        return input_value


class PlayerController(DataController):

    def is_in_json_dataset(self, name: str, last_name: str, birth_date: str):
        """Check with 3 parameters if the new player instance is already exist
         in the json dataset.
        """
        with open('Data/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)
        for i in range(1, len(data_players) + 1):
            if (name == data_players[f"player_{i}"]["name"] and
                    last_name == data_players[f"player_{i}"]["last name"] and
                    birth_date == data_players[f"player_{i}"]["birth date"]):
                return True
        return False

    def export_data_to_json_file(self):
        """Copy the json file in a local dictionary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        with open('Data/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        identify = len(data_players) + 1
        data_players[f"player_{identify}"] = {
            "name": self.name,
            "last name": self.last_name,
            "birth date": self.birth_date
        }
        with open('Data/players.json', 'w') as json_player_file:
            json.dump(data_players, json_player_file)


class TournamentController(DataController):

    # def generate_players_list(self):
    #     players_list: list[Player] = []
    #     for i in range(0, self.players_count):
    #         player_to_add = Player()
    #         players_list.append(player_to_add)
    #     return players_list

    def generate_players_list(self):
        players_list = []
        for i in range(0, self.players_count):
            new_player = Player()
            players_list.append(new_player)

        return players_list
