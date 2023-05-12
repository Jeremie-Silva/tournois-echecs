from app.controllers.round_controller import RoundController
from app.models.tournament import Tournament
from app.views.main_view import MainView
from app.utils import file_opener, object_to_dict, file_writer
from datetime import datetime


class TournamentController:
    """The controller for tournaments"""

    def create_tournament(self, player_controller: object) -> object:
        """The method needs a player controller, it requests the data from the user,
        generates the list of players, notes the start date and creates a tournament"""
        name: str = MainView().get_information_user("Nom du tournoi")
        place: str = MainView().get_information_user("Lieu du tournoi")
        description: str = MainView().get_information_user("description du tournoi")
        number_of_rounds: int = MainView().get_information_user("nombre de rounds", data_type="integer")
        players_count: int = MainView().get_information_user("Nombre de joueurs", data_type="integer")
        date_start: str = str(datetime.now())
        players_list: list[object] = self.create_players_list(players_count, player_controller)
        new_tournament: object = Tournament(
            name=name,
            place=place,
            date_start=date_start,
            description=description,
            number_of_rounds=number_of_rounds,
            players_count=players_count,
            players_list=players_list
        )
        return new_tournament

    def create_players_list(self, players_count: int, player_controller: object) -> list[object]:
        """The method needs a Player Controller and a number of players, it displays the list of players
        and asks the user to indicate which ones are participating,
        it also allows the user to create a new Player if needed"""
        def _select_player() -> object:
            index_player: int = MainView().get_information_user(
                "Numéro du joueur (taper 0 pour ajouter un nouveau joueur)", data_type="integer")
            if index_player == 0:
                player_controller.create_player()
                MainView().print_players_list(player_controller)
                index_player: int = MainView().get_information_user("Numéro du joueur", data_type="integer")
            return getattr(player_controller, f"player_{index_player}")
        players_list: list[object] = []
        MainView().print_players_list(player_controller)
        for index in range(players_count):
            player_selected: object = _select_player()
            players_list.append(player_selected)
        return players_list

    def save_tournament_to_json(self, tournament: object) -> None:
        """The method needs a Tournament, it retrieves the data contained in the tournaments.json file,
        adds the tournament locally while indicating its end date and overwrites the file with the new data """
        data: dict = file_opener("tournaments")
        tournament.date_end = str(datetime.now())
        data[f"tournament_{tournament.name}"] = object_to_dict(tournament)
        file_writer("tournaments", data)

    def run_new_tournament(self, player_controller: object) -> None:
        """The method needs a Player Controller, it launches the creation of a new tournament,
        adds rounds and matches, retrieves scores and saves the tournament"""
        new_tournament: object = self.create_tournament(player_controller)
        tournament: object = RoundController().generate_rounds(new_tournament)
        self.save_tournament_to_json(tournament)
