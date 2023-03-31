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
		self.current_round: int = 1
		self.players_count: int = players_count
		self.players_list: list[Player] = players_list


class Round:
	def __init__(self, round_name: str, list_player: list[Player], list_matchs: list[list[Player]]) -> None:
		self.round_name: str = round_name
		self.list_player: list[Player] = list_player
		self.list_matchs: list[list[Player]] = list_matchs


class Match:
	def __init__(self, round_name: str, player_one: str, player_two: str) -> None:
		self.player_one = player_one
		self.player_two = player_two
		self.score_player_one = 0
		self.score_player_two = 0
		self.match_result = ([player_one, self.score_player_one], [player_two, self.score_player_two])

