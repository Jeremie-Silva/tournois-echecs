from app.controllers.match_controller import MatchController
from app.models.match import Match
from app.models.round import Round
from app.models.tournament import Tournament
from datetime import datetime
from boltons.iterutils import chunked


class RoundController:

    def _generate_matchs(self, tournament):
        current_round = self.get_last_round(tournament)
        if current_round.round_name == "round_1":
            for index, player in enumerate(chunked(src=tournament.players_list, size=2)):
                match_name = f"match_{index+1}"
                try:
                    new_match = Match(match_name, player[0], player[1])
                    setattr(current_round, match_name, new_match)
                    setattr(current_round, "waiting_player", None)
                except IndexError:
                    setattr(current_round, "waiting_player", player[0])
        else:
            sorted_players = self.get_sorted_players_by_score(tournament)
            for index in range(0, len(sorted_players), 2):
                match_name = f"match_{(index // 2) + 1}"
                try:
                    new_match = Match(match_name, sorted_players[index], sorted_players[index + 1])
                    setattr(current_round, match_name, new_match)
                    setattr(current_round, "waiting_player", None)
                except IndexError:
                    setattr(current_round, "waiting_player", sorted_players[index])
        return tournament

    def get_sorted_players_by_score(self, tournament):
        player_scores = {player: 0 for player in tournament.players_list}
        previous_round = self.get_previous_round(tournament)
        player_not_played_last_round = None if previous_round is None else previous_round.waiting_player

        # Calculate cumulative scores for each player
        for round_index in range(1, tournament.number_of_rounds + 1):
            round_name = f"round_{round_index}"
            round = getattr(tournament, round_name, None)
            if round is not None:
                for match_index in range((len(tournament.players_list) + 1) // 2):
                    match_name = f"match_{match_index + 1}"
                    match_obj = getattr(round, match_name, None)
                    if match_obj is not None:
                        player_scores[match_obj.player_one] += match_obj.score_player_one
                        player_scores[match_obj.player_two] += match_obj.score_player_two

        # Sort players by scores
        sorted_players = sorted(tournament.players_list, key=lambda player: player_scores[player], reverse=True)

        # Move player who didn't play last round to the first position
        if player_not_played_last_round is not None:
            sorted_players.remove(player_not_played_last_round)
            sorted_players.insert(0, player_not_played_last_round)

        return sorted_players

    def get_last_round(self, tournament):
        last_round = None
        for index in range(1, tournament.number_of_rounds + 1):
            round_name = f"round_{index}"
            round_obj = getattr(tournament, round_name, None)
            if round_obj is not None:
                last_round = round_obj
            else:
                break
        return last_round

    def get_previous_round(self, tournament):
        current_round = self.get_last_round(tournament)
        if current_round.round_name == "round_1":
            return None  # Il n'y a pas de round précédent pour le premier round
        previous_round_index = int(current_round.round_name.split("_")[1]) - 1
        previous_round_name = f"round_{previous_round_index}"
        previous_round = getattr(tournament, previous_round_name, None)
        return previous_round

    def generate_rounds(self, tournament) -> Tournament:
        for round_index in range(tournament.number_of_rounds):
            round_name = f"round_{round_index + 1}"
            new_round = Round(round_name, tournament.players_list)
            new_round.date_start = str(datetime.now())
            setattr(tournament, round_name, new_round)
            tournament_ready = self._generate_matchs(tournament)
            MatchController().retrieve_scores_round(getattr(tournament, round_name))
            setattr(getattr(tournament, round_name), "date_end", str(datetime.now()))
        return tournament_ready
