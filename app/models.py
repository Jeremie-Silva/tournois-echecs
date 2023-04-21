from boltons.iterutils import chunked


class Player:
	def __init__(self, name: str, last_name: str, birth_date: str, **kwargs) -> None:
		self.name: str = name
		self.last_name: str = last_name
		self.birth_date: str = birth_date
		for key, value in kwargs.items():
			setattr(self, key, value)
	def __str__(self):
		return f"  Nom : {self.name} \n  Prénom : {self.last_name}\n  Date de naissance : {self.birth_date}\n"


class Tournament:
	def __init__(self, name: str, place: str, date_start: str, description: str, number_of_rounds: int, players_count: int, players_list: list[Player]) -> None:
		self.name: str = name
		self.place: str = place
		self.date_start: str = date_start
		self.description: str = description
		self.number_of_rounds: int = number_of_rounds
		self.players_count: int = players_count
		self.players_list: list[Player] = players_list


class Round:
	def __init__(self, round_name: str, players_list) -> None:
		self.round_name: str = round_name
		self.players_list = players_list
		self._generate_matchs()

	def _generate_matchs(self):
		if self.round_name == "round_1":
			for index, player in enumerate(chunked(src=self.players_list, size=2)):
				match_name = f"match_{index+1}"
				try:
					new_match = Match(match_name, player[0], player[1])
					setattr(self, match_name, new_match)
				except:
					pass
		else:
			pass
			#TODO: écrire ce cas et le tester


class Match:
	def __init__(self, match_name: str, player_one: Player, player_two: Player) -> None:
		self.match_name = match_name
		self.player_one = player_one
		self.player_two = player_two
		self.score_player_one: float = 0
		self.score_player_two: float = 0
