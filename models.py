class Player:
	def __init__(self, name: str, last_name: str, birth_date: str) -> None:
		self.name: str = name
		self.last_name: str = last_name
		self.birth_date: str = birth_date


class Tournament:
	def __init__(self, name: str, place: str, date_start: str, date_end: str, description: str, number_of_rounds: int, players_count: int, players_list: list[Player]) -> None:
		self.name: str = name
		self.place: str = place
		self.date_start: str = date_start
		self.date_end: str = date_end
		self.description: str = description
		self.number_of_rounds: int = number_of_rounds
		self.current_round: int = 0
		self.players_count: int = players_count
		self.players_list: list[Player] = players_list


# TODO: poursuivre le dev ici
# class Round:
# 	def __init__(self, player_one: str, player_two: str) -> None:
# 		self.round_name = round_name
# 		self.player_one = player_one
# 		self.player_two = player_two
# 		self.score_one = 0
# 		self.score_two = 0
# 		self.round = ([player_one, self.score_one], [player_two, self.score_two])
