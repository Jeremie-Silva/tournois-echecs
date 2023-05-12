from views.main_view import MainView


class MatchController:
    """The controller for matches"""

    def retrieve_scores_round(self, round: object) -> None:
        """The method needs a round, it scans the round for matches
        and asks the user for the score for each match, it also updates the players' scores"""
        match_index: int = 1
        while True:
            match_name: str = f"match_{match_index}"
            current_match: object = getattr(round, match_name, None)
            if current_match is None:
                break

            result: str = MainView().get_result_match(current_match)
            if result == "joueur 1":
                current_match.score_player_one += 1
            elif result == "joueur 2":
                current_match.score_player_two += 1
            else:
                current_match.score_player_one += 0.5
                current_match.score_player_two += 0.5

            match_index += 1
