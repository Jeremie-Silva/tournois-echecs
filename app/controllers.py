from datetime import datetime
from random import shuffle, randint
from app.models import (
    Player,
    Tournament,
    Round,
    Match
)
from app.utils import (
    file_opener,
    file_writer,
    object_to_dict
)
from app.views import View


class PlayerController:

    def __init__(self):
        self._load_players_from_json()

    def _load_players_from_json(self) -> None:
        data = file_opener("players")
        for player, value in data.items():
            setattr(self, player, Player(**value))

    def create_player(self):
        name = View().get_information_user("Nom du joueur")
        last_name = View().get_information_user("Prénom du joueur")
        birth_date = View().get_information_user("Date de naissance du joueur", data_type="birth_date")
        new_player = Player(name=name, last_name=last_name, birth_date=birth_date)
        self._save_player_to_json(new_player)
        self._load_players_from_json()

    def _save_player_to_json(self, player: Player) -> None:
        """Copy the json file in a local dictionary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        data = file_opener("players")
        identify = len(data)
        data[f"player_{identify}"] = object_to_dict(player)
        file_writer("players", data)


class TournamentController:

    def __init__(self):
        self._load_tournaments_from_json()

    def _load_tournaments_from_json(self):
        pass
        # data = file_opener("tournaments")
        # for tournament, value in data.items():
        #     setattr(self, tournament, Tournament(
        #         name=value['name'], place=value['place'], date_start=value['date start'],
        #         date_end=value['date end']
        #     ))

    def _create_tournament(self, player_controller) -> Tournament:
        name: str = View().get_information_user("Nom du tournoi")
        place: str = View().get_information_user("Lieu du tournoi")
        description: str = View().get_information_user("description du tournoi")
        number_of_rounds: int = View().get_information_user("nombre de rounds", data_type="integer")
        players_count: int = View().get_information_user("Nombre de joueurs", data_type="integer")
        date_start: str = str(datetime.now())
        players_list: list[Player] = self._create_players_list(players_count, player_controller)
        new_tournament = Tournament(
            name=name,
            place=place,
            date_start=date_start,
            description=description,
            number_of_rounds=number_of_rounds,
            players_count=players_count,
            players_list=players_list
        )
        return new_tournament

    def _create_players_list(self, players_count, player_controller) -> list[Player]:
        def _select_player():
            index_player = View().get_information_user("Numéro du joueur (taper 0 pour ajouter un nouveau joueur)", data_type="integer")
            if index_player == 0:
                player_controller.create_player()
                View().print_players_list(player_controller)
                index_player = View().get_information_user("Numéro du joueur", data_type="integer")
            return getattr(player_controller, f"player_{index_player}")
        players_list: list[Player] = []
        View().print_players_list(player_controller)
        for index in range(players_count):
            player_selected = _select_player()
            players_list.append(player_selected)
        return players_list

    def _generate_matchs(self, tournament) -> Tournament:
        for round in range(tournament.number_of_rounds):
            round_name = f"round_{round + 1}"
            new_round = RoundController().generate_matchs(round_name, tournament.players_list)
            setattr(tournament, round_name, new_round)
            RoundController().create_matchs(getattr(tournament, round_name))
        return tournament

    def _retrieve_scores(self, tournament: Tournament) -> Tournament:
        for index_round in range(tournament.number_of_rounds):
            curent_round = getattr(tournament, f"round_{index_round+1}")
            for index_match in range(len(curent_round.list_matchs)):
                try:
                    curent_match = getattr(curent_round, f"match_{index_match+1}")
                    result = View().get_result_match(curent_match)
                    if result == "joueur 1":
                        curent_match.score_player_one += 1
                    elif result == "joueur 2":
                        curent_match.score_player_two += 1
                    else:
                        curent_match.score_player_one += 0.5
                        curent_match.score_player_two += 0.5
                except:
                    pass
        return tournament

    def run_new_tournament(self, player_controller):
        new_tournament = self._create_tournament(player_controller)
        tournament_ready = self._generate_matchs(new_tournament)
        tournament_finish = self._retrieve_scores(tournament_ready)
        # self.save_tournament()
        data = file_opener("tournaments")
        identify = len(data) + 1
        setattr(self, f"tournament_{identify}", tournament_finish)

    def save_tournament_to_json(self):
        data = file_opener("tournaments")
        # TODO: refactoring avec vars(self).items()
        # TODO: mettre des tirets du 8 -> _
        # identify = len(data) + 1
        # data[f"tournament {identify}"] = {
        #     "name": tournament.name,
        #     "place": tournament.place,
        #     "date start": tournament.date_start,
        #     "date end": tournament.date_end,
        #     "description": tournament.description,
        #     "players count": tournament.players_count,
        #     "players list": {},
        #     "number of rounds": tournament.number_of_rounds,
        # }
        # 
        # for player_index in range(len(tournament.players_list)):
        #     data[f"tournament {identify}"]["players list"][f"player {player_index+1}"] = {
        #         "name": tournament.players_list[player_index].name,
        #         "last_name": tournament.players_list[player_index].last_name,
        #         "birth_date": tournament.players_list[player_index].birth_date
        #     }
        # 
        # for round_index in range(tournament.number_of_rounds):
        #     round_data = {}
        #     curent_round = getattr(tournament, f"round_{round_index+1}")
        #     data[f"tournament {identify}"][f"round {round_index+1}"] = {
        #         "round name": curent_round.round_name,
        #     }
        #     for match_index in range(len(curent_round.list_matchs)):
        #         try:
        #             curent_match = getattr(curent_round, f"match_{match_index+1}")
        #             data[f"tournament {identify}"][f"round {round_index+1}"][f"match {match_index+1}"] = {
        #                 "match name": curent_match.match_name,
        #                 "player one": {
        #                     "name": curent_match.player_one.name,
        #                     "last_name": curent_match.player_one.last_name,
        #                     "birth_date": curent_match.player_one.birth_date
        #                 },
        #                 "player two": {
        #                     "name": curent_match.player_two.name,
        #                     "last_name": curent_match.player_two.last_name,
        #                     "birth_date": curent_match.player_two.birth_date
        #                 },
        #                 "score player one": curent_match.score_player_one,
        #                 "score player two": curent_match.score_player_two,
        #             }
        #         except:
        #             pass
        file_writer("tournaments", data)
        return True


class RoundController:

    def generate_matchs(self, round_name: str, players_list: list[Player]) -> Round:
        curent_round = Round(round_name, players_list)
        if curent_round.round_name == "round_1":
            shuffle(curent_round.players_list)
        for index, player in enumerate(players_list):
            match_name = f"match_{index+1}"
            try:
                new_match = Match(match_name, player, players_list[index+1])
                setattr(curent_round, match_name, new_match)
            except:
                pass
        return curent_round

    def create_matchs(self, round: Round):
        current_match = 1
        for match in round.list_matchs:
            match_name = f"match_{current_match}"
            try:
                new_match = Match(match_name, match[0], match[1])
                setattr(round, match_name, new_match)
            except:
                pass
        return round
