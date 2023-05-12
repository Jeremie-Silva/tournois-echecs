import datetime
from typing import Literal, Tuple


MENU_CHOICES: list[int] = [0, 1, 2, 3]
REPORT_CHOICES: dict[str, str] = {
    "1": "players_sorted_by_name",
    "2": "tournaments_list",
    "3": "tournament_selected_name_date",
    "4": "tournament_players_list_sorted_by_name",
    "5": "tournament_matchs_list"
}


class MainView:
    """The main view by default"""

    def main_menu(self) -> int:
        """The method display the main menu and retrieves the user's choice,
        checks its validity and returns it"""
        input_choice: int = 99999
        while int(input_choice) not in MENU_CHOICES:
            self.print_title("MENU")
            print("Voici la liste des choix possible :")
            print("1 : Enregistrer un nouveau JOUEUR")
            print("2 : Enregistrer un nouveau TOURNOI")
            print("3 : Afficher un RAPPORT")
            print("0 : Quitter")
            try:
                input_choice: int = int(input("Veuillez saisir un chiffre : "))
                if input_choice in MENU_CHOICES:
                    break
                else:
                    print("-Erreur- Choix invalide")
            except ValueError:
                print("-Erreur- Format invalide")
        print(" Choix valide !")
        print("---------------------------------------")
        return input_choice

    def report_menu(self) -> Tuple[str, str]:
        """The method displays the menu of reports, retrieves the user's choice, checks its validity,
        retrieves also if needed the name of a tournament and returns the two values"""
        input_choice: int = 99999
        tournament_name: str = ""
        while int(input_choice) not in REPORT_CHOICES:
            self.print_title("RAPPORTS")
            print("Quel rapport voulez-vous afficher?")
            print("1 : Liste des joueurs triée par nom")
            print("2 : Liste des tournois")
            print("3 : Nom et date du tournoi sélectionné")
            print("4 : Liste des joueurs du tournoi sélectionné, triée par nom")
            print("5 : Liste de tous les matchs du tournoi sélectionné")
            try:
                input_choice: int = int(input("Veuillez saisir un chiffre : "))
                if input_choice in [int(key) for key, value in REPORT_CHOICES.items()]:
                    match input_choice:
                        case 3 | 4 | 5:
                            try:
                                tournament_name: str = str(input("Veuillez saisir le nom d'un tournoi : "))
                            except ValueError:
                                print("-Erreur- Format invalide")
                    break
                else:
                    print("-Erreur- Choix invalide")
            except ValueError:
                print("-Erreur- Format invalide")
            print(" Choix valide !")
            print("---------------------------------------")
        return REPORT_CHOICES[f"{input_choice}"], tournament_name

    def get_information_user(
            self, message: str, data_type: Literal["string", "birth_date", "integer"] = "string"
    ) -> str | int:
        """The method needs a custom message and a data type, it chooses string by default.
        It allows to retrieve information from the user,
        it makes different checks according to the type of data and returns the value if it is valid"""
        while True:
            if data_type == "string":
                try:
                    input_value: str = str(input(f"{message} : "))
                    if all(char.isalpha() or char.isspace() for char in input_value) and len(input_value) < 100:
                        break
                except ValueError:
                    pass
            elif data_type == "birth_date":
                print(f"{message} : ")
                try:
                    input_year: str = str(input("Année : "))
                    input_month: str = str(input("Mois : "))
                    input_day: str = str(input("Jour : "))
                    if (input_year.isdigit() and len(input_year) == 4 and
                            input_month.isdigit() and len(input_month) == 2 and int(input_month) <= 12 and
                            input_day.isdigit() and len(input_day) == 2 and int(input_day) <= 31):
                        input_value: str = str(datetime.date(int(input_year), int(input_month), int(input_day)))
                        break
                except ValueError:
                    pass
            elif data_type == "integer":
                try:
                    input_value: int = int(input(f"{message} : "))
                    if (str(input_value).isdigit() and len(str(input_value)) == 1 or
                            len(str(input_value)) == 2):
                        break
                except ValueError:
                    pass
            else:
                raise ValueError
            print(f"-Erreur- {message} invalide")
        return input_value

    def get_result_match(self, match: object) -> str:
        """The method needs a Match, it displays the match information to the user
        and asks for the match result. If the input is valid, it returns a string containing the result"""
        while True:
            self.print_title(match.match_name.upper())
            print("JOUEUR 1 (taper 1)")
            print(match.player_one)
            print("JOUEUR 2 (taper 2)")
            print(match.player_two)
            print("MATCH NUL (taper 0) \n")
            try:
                input_choice: int = int(input("Veuillez saisir le resultat : "))
                match input_choice:
                    case 0 | 1 | 2:
                        break
                    case _:
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

    def print_players_list(self, player_controller: object) -> None:
        """The method needs a player controller, it iterates through it
        and displays all the players contained, except the admin"""
        for key, value in vars(player_controller).items():
            if key != 'player_0':
                print(key)
                print(value)

    def print_title(self, title: str) -> None:
        """The method needs a title, it displays this title in the console
        and surrounds it with a decoration"""
        len_title: int = 40
        symbol: str = "-"
        print("\n"+symbol*len_title)
        print(symbol*int(len_title/2-len(title)/2)+title+symbol*int(len_title/2-len(title)/2))
        print(symbol*len_title+"\n")
