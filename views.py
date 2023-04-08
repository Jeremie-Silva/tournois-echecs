import datetime
from typing import Literal
from models import Match

MENU_CHOICES: list[int] = [1, 2]


class View:

    def main_menu(self) -> None:
        input_choice = 0
        while int(input_choice) not in MENU_CHOICES:
            print("-------------------------------------")
            print("Voici la liste des choix possible :")
            print("1 : Enregistrer un nouveau TOURNOI")
            try:
                input_choice = int(input("Veuillez saisir un chiffre : "))
                if input_choice in MENU_CHOICES:
                    break
                else:
                    print("-Erreur- Choix invalide")
            except ValueError:
                print("-Erreur- Format invalide")
        print(" Choix valide !")
        print("-------------------------------------")
        if input_choice == 1:
            print("Création de JOUEUR :")
        elif input_choice == 2:
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

    def get_result_match(self, match: Match):
        input_choice = 0
        while int(input_choice) != 1 or int(input_choice) != 2:
            print(f"-----{match.match_name.upper()}-----\n")
            print("JOUEUR 1 : tapez 1")
            print(match.player_one)
            print("JOUEUR 2 : tapez 2")
            print(match.player_two)
            print("MATCH NUL : tapez 0 \n")
            try:
                input_choice = int(input("Veuillez saisir le resultat : "))
                if input_choice == 0 or input_choice == 1 or input_choice == 2:
                    break
                else:
                    print("-Erreur- Choix invalide")
            except ValueError:
                print("-Erreur- Format invalide")
        print(" Choix valide !")
        print("-------------------------------------")
        if input_choice == 1:
            return "joueur 1"
        elif input_choice == 2:
            return "joueur 2"
        else:
            return "nul"

    def print_players_list(player_controller):
        for key in vars(player_controller):
            print(key)
            print(vars(player_controller)[key])