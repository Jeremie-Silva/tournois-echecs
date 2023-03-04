from Controllers.player_controller import PlayerController


class Player(PlayerController):
    def __init__(self):
        self.name: str = self.get_information_player_str("Nom du joueur")
        self.last_name: str = self.get_information_player_str("Prénom du joueur")
        self.birth_date: int = self.get_information_player_int("Date de naissance du joueur (exemple: 24122023)")
