from Models.player import Player


def main_menu():
    input_choice = 0
    valid_choices: list[int] = [1]

    while int(input_choice) not in valid_choices:
        print("-------------------------------------")
        print("Voici la liste des choix possible :")
        print("1 : Enregistrer un nouveau joueur")
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

    bring_user_to_choice(input_choice)


def bring_user_to_choice(input_choice: int):
    if input_choice == 1:
        new_player = Player()
        if not new_player.is_in_json_dataset(
                new_player.name,
                new_player.last_name,
                new_player.birth_date):
            new_player.export_data_to_json_file()
#TODO: ajouter les autres possibilitées dans le menu  
