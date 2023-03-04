import json
from Models.player import Player


class TournamentController(Player):

    def get_information_tournament_str(self, message: str):
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        while True:
            try:
                input_value = str(input(f"{message} : "))
            except ValueError:
                pass
            if input_value.isalpha() and len(input_value) < 100:
                break
            print(f"-Erreur- {message} invalide")
        return input_value

    def generate_players_list(self):
        players_list: list[Player] = []
        for i in range(0, self.players_count):
            player_to_add = Player()
            players_list.append(player_to_add)
        return players_list
