from app.models.player import Player


class Tournament:
    def __init__(self, name: str, place: str, date_start: str, description: str,
                 number_of_rounds: int, players_count: int, players_list: list[Player]
                 ) -> None:
        self.name: str = name
        self.place: str = place
        self.date_start: str = date_start
        self.description: str = description
        self.number_of_rounds: int = number_of_rounds
        self.players_count: int = players_count
        self.players_list: list[Player] = players_list
