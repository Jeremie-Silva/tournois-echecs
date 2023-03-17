import json
import datetime
from typing import Literal
from models import (
    Player,
    Tournament,
)


class DataController:

    def get_information_user(self, message: str, data_type: Literal["string", "day_date", "integer"] = "string") -> str|int:
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

    def _player_is_in_json_dataset(self, name: str, last_name: str, birth_date: str) -> bool:
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

    def _export_player_to_json_file(self, name: str, last_name: str, birth_date: str) -> None:
        """Copy the json file in a local dictionary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        with open('Data/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        identify = len(data_players) + 1
        data_players[f"player_{identify}"] = {
            "name": name,
            "last name": last_name,
            "birth date": birth_date
        }
        with open('Data/players.json', 'w') as json_player_file:
            json.dump(data_players, json_player_file)

    def create_player(self) -> Player:
        name = self.get_information_user("Nom du joueur")
        last_name = self.get_information_user("Prénom du joueur")
        birth_date = self.get_information_user("Date de naissance du joueur (exemple: 24122023)", data_type="day_date")
        new_player = Player(
            name=name,
            last_name=last_name,
            birth_date=birth_date
        )
        return new_player

    def save_player(self, Player) -> bool:
        if not self._player_is_in_json_dataset(
            Player.name,
            Player.last_name,
            Player.birth_date
        ):
            self._export_player_to_json_file(
                Player.name,
                Player.last_name,
                Player.birth_date
            )
        return True


class TournamentController(DataController):

    def create_tournament(self):
        name: str = self.get_information_user("Nom du tournoi")
        place: str = self.get_information_user("Lieu du tournoi")
        date_start: str = self.get_information_user("date de début du tournoi", data_type="day_date")
        date_end: str = self.get_information_user("date de fin du tournoi", data_type="day_date")
        description: str = self.get_information_user("description du tournoi")
        number_of_rounds: int = self.get_information_user("nombre de rounds", data_type="integer")
        players_count: int = self.get_information_user("Nombre de joueurs", data_type="integer")
        players_list: list[Player] = self.generate_players_list(players_count)
        new_tournament = Tournament(
            name=name,
            place=place,
            date_start=date_start,
            date_end=date_end,
            description=description,
            number_of_rounds=number_of_rounds,
            players_count=players_count,
            players_list=players_list
        )
        return new_tournament

    def generate_players_list(self, players_count) -> list[Player]:
        players_list: list[Player] = []
        for i in range(players_count):
            new_player: Player = PlayerController().create_player()
            PlayerController().save_player(new_player)
            players_list.append(new_player)
        return players_list


