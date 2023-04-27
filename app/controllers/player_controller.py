from app.models.player import Player
from app.views.main_view import MainView
from app.utils import file_opener, object_to_dict, file_writer


class PlayerController:

    def __init__(self):
        self._load_players_from_json()

    def _load_players_from_json(self) -> None:
        data = file_opener("players")
        for player, value in data.items():
            setattr(self, player, Player(**value))

    def _save_player_to_json(self, player: Player) -> None:
        """Copy the json file in a local dictionary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        data = file_opener("players")
        identify = len(data)
        data[f"player_{identify}"] = object_to_dict(player)
        file_writer("players", data)

    def create_player(self):
        name = MainView().get_information_user("Nom du joueur")
        last_name = MainView().get_information_user("Prénom du joueur")
        birth_date = MainView().get_information_user("Date de naissance du joueur", data_type="birth_date")
        new_player = Player(name=name, last_name=last_name, birth_date=birth_date)
        self._save_player_to_json(new_player)
        self._load_players_from_json()
