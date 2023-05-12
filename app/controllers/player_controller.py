from app.models.player import Player
from app.views.main_view import MainView
from app.utils import file_opener, object_to_dict, file_writer


class PlayerController:
    """The controller for players"""

    def __init__(self) -> None:
        """The constructor does not need any information
        and launches the initialization method which instantiates all the players"""
        self.load_players_from_json()

    def load_players_from_json(self) -> None:
        """The method does not need any information, it retrieves the data contained in the players.json file
        and instantiates all the players with the right data"""
        data: dict = file_opener("players")
        for player, value in data.items():
            setattr(self, player, Player(**value))

    def save_player_to_json(self, player: object) -> None:
        """The method needs a player, it retrieves the data contained in the players.json file,
        adds the player locally with an identifier and overwrites the file with the new data"""
        data: dict = file_opener("players")
        identify: int = len(data)
        data[f"player_{identify}"] = object_to_dict(player)
        file_writer("players", data)

    def create_player(self) -> None:
        """The method doesn't need any parameters, it asks the user for the information
        and instantiates a Player with this data, saves the Player in the json file
        and restarts the controller initialization method"""
        name: str = MainView().get_information_user("Nom du joueur")
        last_name: str = MainView().get_information_user("Prénom du joueur")
        birth_date: str = MainView().get_information_user("Date de naissance du joueur", data_type="birth_date")
        new_player: object = Player(name=name, last_name=last_name, birth_date=birth_date)
        self.save_player_to_json(new_player)
        self.load_players_from_json()
