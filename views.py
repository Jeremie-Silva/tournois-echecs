import datetime
from typing import Literal

VALID_CHOICES: list[int] = [1]


class View:

    def main_menu(self) -> None:
        input_choice = 0
        while int(input_choice) not in VALID_CHOICES:
            print("-------------------------------------")
            print("Voici la liste des choix possible :")
            print("1 : Enregistrer un nouveau TOURNOI")
            try:
                input_choice = int(input("Veuillez saisir un chiffre : "))
                if input_choice in VALID_CHOICES:
                    break
                else:
                    print("-Erreur- Choix invalide")
            except ValueError:
                print("-Erreur- Format invalide")
        print(" Choix valide !")
        print("-------------------------------------")
        if input_choice == 1:
            print("Création du TOURNOI :")
        return input_choice

    def get_information_user(self, message: str, data_type: Literal["string", "day_date", "integer"] = "string") -> str|int:
        """Ask the information from the user,
        print a custom message,
        checks the validity and return it
        """
        input_value: str = ""
        input_year: str = ""
        input_month: str = ""
        input_day: str = ""
        while True:
            if data_type == "string":
                try:
                    input_value = str(input(f"{message} : "))
                    if input_value.isalpha() and len(input_value) < 100:
                        break
                except ValueError:
                    pass
            elif data_type == "day_date":
                print(f"{message} : ")
                try:
                    input_year = str(input("Année : "))
                    input_month = str(input("Mois : "))
                    input_day = str(input("Jour : "))
                    if (input_year.isdigit() and len(input_year) == 4 and
                        input_month.isdigit() and len(input_month) == 2 and int(input_month) <= 12 and
                        input_day.isdigit() and len(input_day) == 2 and int(input_day) <= 31
                    ):
                        input_value = str(datetime.date(int(input_year), int(input_month), int(input_day)))
                        break
                except ValueError:
                    pass
            elif data_type == "integer":
                try:
                    input_value = int(input(f"{message} : "))
                    if (str(input_value).isdigit() and len(str(input_value)) == 1 or
		                    len(str(input_value)) == 2):
                        break
                except ValueError:
                    pass
            else:
                raise ValueError
            print(f"-Erreur- {message} invalide")
        return input_value

    def get_result(self):
        # TODO: recupérer les résultats
        pass
