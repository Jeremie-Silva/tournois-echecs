from Controllers.tournament_controller import TournamentController
from Models.player import Player


class Tournament(TournamentController):
    def __init__(self):
        self.name: str = self.get_information_tournament_str("Nom du tournoi")
        self.place: str = self.get_information_tournament_str("Lieu du tournoi")
        self.date_start: str = self.get_information_tournament_str("date de début du tournoi")
        # TODO: Utiliser la librairie datetime
        self.date_end: str = self.get_information_tournament_str("date de fin du tournoi")
        self.description: str = self.get_information_tournament_str("description du tournoi")
        self.number_of_rounds: int = 4
        self.current_round: int = 0
        self.players_count: int = self.get_information_player_int("Nombre de joueurs")
        self.players_list:list[Player] = self.generate_players_list()
        print(self.players_list)
        # self.rounds_list = self.generate_rounds_list()
