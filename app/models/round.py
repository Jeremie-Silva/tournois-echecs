class Round:
    """The model for rounds"""

    def __init__(self, round_name: str, players_list: list[object]) -> None:
        """The builder needs a round name and a list of Players"""
        self.round_name: str = round_name
        self.players_list: list[object] = players_list
