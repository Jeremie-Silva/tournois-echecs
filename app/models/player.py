class Player:
	def __init__(self, name: str, last_name: str, birth_date: str, **kwargs) -> None:
		self.name: str = name
		self.last_name: str = last_name
		self.birth_date: str = birth_date
		for key, value in kwargs.items():
			setattr(self, key, value)
	def __str__(self):
		return f"  Nom : {self.name} \n  Prénom : {self.last_name}\n  Date de naissance : {self.birth_date}\n"
