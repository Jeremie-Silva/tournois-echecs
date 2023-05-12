class Match:
    """The model for matches"""

    def __init__(self, match_name: str, player_one: object, player_two: object) -> None:
        """The builder needs a match name and two Player objects,
        it creates by default the score attributes and initializes them to zero"""
        self.match_name: str = match_name
        self.player_one: object = player_one
        self.player_two: object = player_two
        self.score_player_one: float = 0
        self.score_player_two: float = 0
