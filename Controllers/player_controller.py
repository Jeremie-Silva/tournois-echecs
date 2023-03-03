import json


class PlayerController:

    def set_information_player(self):
        """Ask the information from the user,
        checks the validity and stores it in the self
        """
        name_input: str = ""
        while True:
            try:
                name_input = str(input("Nom du joueur : "))
            except ValueError:
                pass
            if name_input.isalpha() and len(name_input) < 100:
                self.name = name_input
                break
            print("-Erreur- Nom invalide")

        last_name_input: str = ""
        while True:
            try:
                last_name_input = str(input("Prénom du joueur : "))
            except ValueError:
                pass
            if last_name_input.isalpha() and len(last_name_input) < 100:
                self.last_name = last_name_input
                break
            print("-Erreur- Prénom invalide")

        birth_date_input: int = 0
        while True:
            try:
                birth_date_input = int(input("Date de naissance du joueur : "))
            except ValueError:
                pass
            if len(str(birth_date_input)) == 8:
                self.birth_date = birth_date_input
                break
            print("-Erreur- Date invalide (exemple: 24122023)")

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