class Tournament:
    """The model for tournaments"""

    def __init__(self, name: str, place: str, date_start: str, description: str,
                 number_of_rounds: int, players_count: int, players_list: list[object]
                 ) -> None:
        """The builder needs a name, a place, a date of start, a description,
        a number of rounds, number of players and a list of Players"""
        self.name: str = name
        self.place: str = place
        self.date_start: str = date_start
        self.description: str = description
        self.number_of_rounds: int = number_of_rounds
        self.players_count: int = players_count
        self.players_list: list[object] = players_list
