class Player:
    """The model for players"""

    def __init__(self, name: str, last_name: str, birth_date: str, **kwargs) -> None:
        """The builder needs a name, a first name, a date of birth
        and eventually takes additional parameters"""
        self.name: str = name
        self.last_name: str = last_name
        self.birth_date: str = birth_date
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """The str method returns a sentence containing the name,
        the first name and the date of birth of the Player"""
        return f"  Nom : {self.name} \n  Prénom : {self.last_name}\n  Date de naissance : {self.birth_date}\n"
