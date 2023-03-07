import json
import datetime


class DataController:
    def get_information_user(self, message: str, data_type: str = "string"):
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        while True:
            # TODO: Utiliser la valeur Literal (import)
            if data_type == "string":
                try:
                    input_value = str(input(f"{message} : "))
                except ValueError:
                    pass
                if input_value.isalpha() and len(input_value) < 100:
                    break
            if data_type == "birth_date":
                input_year = ""
                input_month = ""
                input_day = ""
                try:
                    input_year = str(input("Année de naissance : "))
                    input_month = str(input("Mois de naissance : "))
                    input_day = str(input("Jour de naissance : "))
                except:
                    input_value = datetime(input_year, input_month, input_day)
                # TODO: FINIR IMPORT DATETIME
            else:
                try:
                    input_value = int(input(f"{message} : "))
                except ValueError:
                    pass
                if len(str(input_value)) == 1 or len(str(input_value)) == 2 and str(input_value).isdigit():
                    break
            print(f"-Erreur- {message} invalide")
        return input_value

class PlayerController(DataController):

    def is_in_json_dataset(self, name: str, last_name: str, birth_date: int):
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

    def generate_players_list(self):
        # TODO: Poursuivre le DEV
        pass
    #     players_list: list[Player] = []
    #     for i in range(0, self.players_count):
    #         player_to_add = Player()
    #         players_list.append(player_to_add)
    #     return players_list