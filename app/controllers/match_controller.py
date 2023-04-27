from app.views.main_view import MainView


class MatchController:

	def _retrieve_scores_round(self, round):
		match_index = 1
		while True:
			match_name = f"match_{match_index}"
			current_match = getattr(round, match_name, None)
			if current_match is None:
				break

			result = MainView().get_result_match(current_match)
			if result == "joueur 1":
				current_match.score_player_one += 1
			elif result == "joueur 2":
				current_match.score_player_two += 1
			else:
				current_match.score_player_one += 0.5
				current_match.score_player_two += 0.5

			match_index += 1
