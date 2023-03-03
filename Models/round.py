class Round:
    def __init__(self, player_one:str, player_two:str):
        self.round_name = self.generate_round_name()
        self.player_one = player_one
        self.player_two = player_two
        self.score_one = 0
        self.score_two = 0
        self.round = ([player_one, self.score_one],[player_two, self.score_two])

    # def generate_round_name():
    #     pass
