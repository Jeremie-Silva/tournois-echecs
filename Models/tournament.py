class Tournament:
    def __init__(self, name:str, place:str, date_start:str, date_end:str, 
                description:str, number_of_rounds:int=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.description = description
        self.players_list = self.generate_players_list()
        self.rounds_list = self.generate_rounds_list()


    def generate_players_list(self):
        # TODO
        pass

    def generate_rounds_list(self):
        pass

