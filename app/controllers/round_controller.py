from app.controllers.match_controller import MatchController
from app.models.match import Match
from app.models.round import Round
from datetime import datetime
from boltons.iterutils import chunked


class RoundController:
    """The controller for rounds"""

    def generate_matchs(self, tournament: object) -> object:
        """The method needs a Tournament, it retrieves the last round and creates the matches of this round,
        if it is the first round then it generates the pairs by chance,
        otherwise it associates the players according to their score in the tournament"""
        current_round: object = self.get_last_round(tournament)
        if current_round.round_name == "round_1":
            for index, player in enumerate(chunked(src=tournament.players_list, size=2)):
                match_name: str = f"match_{index+1}"
                try:
                    new_match: object = Match(match_name, player[0], player[1])
                    setattr(current_round, match_name, new_match)
                    setattr(current_round, "waiting_player", None)
                except IndexError:
                    setattr(current_round, "waiting_player", player[0])
        else:
            sorted_players: list = self.get_sorted_players_by_score(tournament)
            for index in range(0, len(sorted_players), 2):
                match_name: str = f"match_{(index // 2) + 1}"
                try:
                    new_match: object = Match(match_name, sorted_players[index], sorted_players[index + 1])
                    setattr(current_round, match_name, new_match)
                    setattr(current_round, "waiting_player", None)
                except IndexError:
                    setattr(current_round, "waiting_player", sorted_players[index])
        return tournament

    def get_sorted_players_by_score(self, tournament: object) -> list:
        """The method needs a Tournament,
        it generates a list of players ranked by score since the beginning of the tournament"""
        player_scores: dict = {player: 0 for player in tournament.players_list}
        previous_round: object = self.get_previous_round(tournament)
        player_not_played_last_round: object = None if previous_round is None else previous_round.waiting_player
        for round_index in range(1, tournament.number_of_rounds + 1):
            round_name: str = f"round_{round_index}"
            round: object | None = getattr(tournament, round_name, None)
            if round is not None:
                for match_index in range((len(tournament.players_list) + 1) // 2):
                    match_name: str = f"match_{match_index + 1}"
                    match_obj: object = getattr(round, match_name, None)
                    if match_obj is not None:
                        player_scores[match_obj.player_one] += match_obj.score_player_one
                        player_scores[match_obj.player_two] += match_obj.score_player_two
        sorted_players: list = sorted(tournament.players_list, key=lambda player: player_scores[player], reverse=True)
        if player_not_played_last_round is not None:
            sorted_players.remove(player_not_played_last_round)
            sorted_players.insert(0, player_not_played_last_round)
        return sorted_players

    def get_last_round(self, tournament: object) -> object:
        """The method needs a Tournament, it inspects the tournament and returns the last round"""
        last_round: None = None
        for index in range(1, tournament.number_of_rounds + 1):
            round_name: str = f"round_{index}"
            round_obj: object = getattr(tournament, round_name, None)
            if round_obj is not None:
                last_round: object = round_obj
            else:
                break
        return last_round

    def get_previous_round(self, tournament: object) -> object:
        """The method needs a Tournament, it inspects the tournament and returns the previous round"""
        current_round: object = self.get_last_round(tournament)
        if current_round.round_name == "round_1":
            return None
        previous_round_index: int = int(current_round.round_name.split("_")[1]) - 1
        previous_round_name: str = f"round_{previous_round_index}"
        previous_round: object = getattr(tournament, previous_round_name, None)
        return previous_round

    def generate_rounds(self, tournament: object) -> object:
        """The method needs a Tournament, it generates the rounds and their matches,
        then asks the user for the results, adding the start and end date of the round"""
        for round_index in range(tournament.number_of_rounds):
            round_name: str = f"round_{round_index + 1}"
            new_round: object = Round(round_name, tournament.players_list)
            new_round.date_start = str(datetime.now())
            setattr(tournament, round_name, new_round)
            tournament_ready: object = self.generate_matchs(tournament)
            MatchController().retrieve_scores_round(getattr(tournament, round_name))
            setattr(getattr(tournament, round_name), "date_end", str(datetime.now()))
        return tournament_ready
