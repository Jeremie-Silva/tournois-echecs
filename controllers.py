import json
from boltons.iterutils import chunked
from random import shuffle
from models import (
    Player,
    Tournament,
    Round,
    Match
)
from views import View


class PlayerController:

    def _player_is_in_json_dataset(self, name: str, last_name: str, birth_date: str) -> bool:
        """Check with 3 parameters if the new player instance is already exist
         in the json dataset.
        """
        with open('Data/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)
        for i in range(1, len(data_players) + 1):
            if (name == data_players[f"player_{i}"]["name"] and
                    last_name == data_players[f"player_{i}"]["last name"] and
                    birth_date == data_players[f"player_{i}"]["birth date"]):
                return True
        return False

    def _export_player_to_json_file(self, name: str, last_name: str, birth_date: str) -> None:
        """Copy the json file in a local dictionary for add a new player
        and resend the new dict into the json file.
        Create an incremental name.
        """
        with open('Data/players.json', 'r') as json_player_file:
            data_players = json.load(json_player_file)

        identify = len(data_players) + 1
        data_players[f"player_{identify}"] = {
            "name": name,
            "last name": last_name,
            "birth date": birth_date
        }
        with open('Data/players.json', 'w') as json_player_file:
            json.dump(data_players, json_player_file)

    def create_player(self) -> Player:
        # name = View().get_information_user("Nom du joueur")
        # last_name = View().get_information_user("Prénom du joueur")
        # birth_date = View().get_information_user("Date de naissance du joueur (exemple: 24122023)", data_type="day_date")
        name = "playername"
        last_name = "playerlastname"
        birth_date = "playerbirthdate"
        new_player = Player(
            name=name,
            last_name=last_name,
            birth_date=birth_date
        )
        return new_player

    def save_player(self, Player) -> bool:
        if not self._player_is_in_json_dataset(
            Player.name,
            Player.last_name,
            Player.birth_date
        ):
            self._export_player_to_json_file(
                Player.name,
                Player.last_name,
                Player.birth_date
            )
        return True


class TournamentController:

    def _create_tournament(self) -> Tournament:
        # name: str = View().get_information_user("Nom du tournoi")
        # place: str = View().get_information_user("Lieu du tournoi")
        # date_start: str = View().get_information_user("date de début du tournoi", data_type="day_date")
        # date_end: str = View().get_information_user("date de fin du tournoi", data_type="day_date")
        # description: str = View().get_information_user("description du tournoi")
        # number_of_rounds: int = View().get_information_user("nombre de rounds", data_type="integer")
        # players_count: int = View().get_information_user("Nombre de joueurs", data_type="integer")
        name: str = "name"
        place: str = "place"
        date_start: str = "date_start"
        date_end: str = "date_end"
        description: str = "description"
        number_of_rounds: int = 4
        players_count: int = 2
        players_list: list[Player] = self._create_players_list(players_count)
        new_tournament = Tournament(
            name=name,
            place=place,
            date_start=date_start,
            date_end=date_end,
            description=description,
            number_of_rounds=number_of_rounds,
            players_count=players_count,
            players_list=players_list
        )
        return new_tournament

    def _create_players_list(self, players_count) -> list[Player]:
        players_list: list[Player] = []
        for i in range(players_count):
            new_player: Player = PlayerController().create_player()
            PlayerController().save_player(new_player)
            players_list.append(new_player)
        return players_list

    def _generate_matchs(self, tournament) -> Tournament:
        current_round = 1
        for round in range(tournament.number_of_rounds):
            round_name = f"round_{current_round}"
            new_round = RoundController().create_round(round_name, tournament.players_list)
            setattr(tournament, round_name, new_round)
            RoundController().create_matchs(getattr(tournament, round_name))
            current_round += 1
        return tournament

    def _retrieve_scores(self, tournament: Tournament) -> Tournament:
        for round in range(tournament.number_of_rounds):
            curent_round = getattr(tournament, f"round_{round+1}")
            for match in range(len(curent_round.list_matchs)):
                curent_match = getattr(curent_round, f"match_{match+1}")
                if View().get_result_match(curent_match) == "joueur 1":
                    getattr(curent_match, f"match_{match+1}")
                    # TODO: poursuivre ici
        return tournament


    def run_new_tournament(self):
        new_tournament = self._create_tournament()
        tournament_ready = self._generate_matchs(new_tournament)
        tournament_finish = self._retrieve_scores(tournament_ready)


class RoundController:

    def create_round(self, round_name: str, players_list: list[Player]) -> Round:
        shuffle(players_list)
        list_matches = [tuple(match) for match in chunked(players_list, 2)]
        return Round(round_name, players_list, list_matches)

    def create_matchs(self, round: Round):
        current_match = 1
        for match in round.list_matchs:
            match_name = f"match_{current_match}"
            new_match = Match(match_name, match[0], match[1])
            setattr(round, match_name, new_match)
        return round
