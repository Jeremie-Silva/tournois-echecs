import json
from Controllers.data_controller import DataController


class PlayerController(DataController):

    def get_information_player_str(self, message: str):
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        while True:
            try:
                input_value = str(input(f"{message} : "))
                # :TODO refactorer les 2 methode en une, créer des sous méthodes "is value valid"
                if input_value.isalpha() and len(input_value) < 100:
                    break
            except ValueError:
                pass
            print(f"-Erreur- {message} invalide")
        return input_value
        #TODO: global controller ?

    def get_information_player_int(self, message: str):
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        while True:
            try:
                input_value = int(input(f"{message} : "))
                if len(str(input_value)) == 1 or len(str(input_value)) == 2 and str(input_value).isdigit():
                    break
            except ValueError:
                pass
            print(f"-Erreur- {message} invalide ")
        return input_value

    def is_in_json_dataset(self, name: str, last_name: str, birth_date: int):
        """Check with 3 parameters if the new player instance is already exist
         in the json dataset.
        """
        with open('Data/Players/players.json', 'r') as json_player_file:
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
        with open('Data/Players/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        identify = len(data_players) + 1
        data_players[f"player_{identify}"] = {
            "name": self.name,
            "last name": self.last_name,
            "birth date": self.birth_date
        }
        with open('Data/Players/players.json', 'w') as json_player_file:
            json.dump(data_players, json_player_file)

    #TODO: debug cette méthode

    # def instance_player_from_json_dataset(self, name_input, last_name_input):
    #     with open('Data/Players/players.json', 'r') as json_player_file:
    #         data_players = json.load(json_player_file)
    # 
    #     for i in range(1, len(data_players) + 1):
    #         if (name_input == data_players[f"player_{i}"]["name"] and
    #                 last_name_input == data_players[f"player_{i}"][
    #                     "last name"]):
    #             birth_date_dataset = data_players[f"player_{i}"]["birth date"]
    #             Player(name_input, last_name_input, birth_date_dataset)
    #             print("ouiiiii")
    #         else:
    #             print("noooon")
    # 
    #     return

    #TODO: ajouter le controller de Tournament