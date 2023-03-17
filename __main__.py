from controllers import (
    PlayerController,
    TournamentController
)


def main_menu() -> None:
    input_choice = 0
    valid_choices: list[int] = [1]
    while int(input_choice) not in valid_choices:
        print("-------------------------------------")
        print("Voici la liste des choix possible :")
        print("1 : Enregistrer un nouveau TOURNOI")
        try:
            input_choice = int(input("Veuillez saisir un chiffre : "))
            if input_choice in valid_choices:
                break
            else:
                print("-Erreur- Choix invalide")
        except ValueError:
            print("-Erreur- Format invalide")

    print(" Choix valide !")
    print("-------------------------------------")
    if input_choice == 1:
        print("Création du TOURNOI :")
        tournament_controller.create_tournament()


tournament_controller = TournamentController()

if __name__ == '__main__':
    main_menu()
