from Controllers.player_controller import PlayerController


class Player(PlayerController):
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.birth_date = 0
        self.set_information_player()
