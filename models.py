from controllers import (
    PlayerController,
    TournamentController
)


class Player(PlayerController):
    def __init__(self):
        self.name: str = self.get_information_user("Nom du joueur")
        self.last_name: str = self.get_information_user("Prénom du joueur")
        self.birth_date: int = self.get_information_user(
            "Date de naissance du joueur (exemple: 24122023)", data_type="date")
        # TODO: Utiliser la librairie datetime

class Tournament(TournamentController):
    def __init__(self):
        self.name: str = self.get_information_user("Nom du tournoi")
        self.place: str = self.get_information_user("Lieu du tournoi")
        self.date_start: str = self.get_information_user("date de début du tournoi")
        # TODO: Utiliser la librairie datetime
        self.date_end: str = self.get_information_user("date de fin du tournoi")
        # TODO: Utiliser la librairie datetime
        self.description: str = self.get_information_user("description du tournoi")
        self.number_of_rounds: int = 4
        # TODO: Traiter le cas ou l'on peut modifier le nombre de rounds
        self.current_round: int = 0
        self.players_count: int = self.get_information_user("Nombre de joueurs", data_type="integer")
        # self.players_list: list[Player] = self.generate_players_list()
        # self.rounds_list = self.generate_rounds_list()

class Round:
    def __init__(self, player_one:str, player_two:str):
        # self.round_name = self.generate_round_name()
        self.player_one = player_one
        self.player_two = player_two
        self.score_one = 0
        self.score_two = 0
        self.round = ([player_one, self.score_one],[player_two, self.score_two])
