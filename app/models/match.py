from app.models.player import Player


class Match:
    def __init__(self, match_name: str, player_one: Player, player_two: Player) -> None:
        self.match_name = match_name
        self.player_one = player_one
        self.player_two = player_two
        self.score_player_one: float = 0
        self.score_player_two: float = 0
