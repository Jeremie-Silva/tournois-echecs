from app.controllers import (
    TournamentController,
    PlayerController
)
from app.views import View


def app_running():
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    input_choice = View().main_menu()
    # input_choice = 2
    if input_choice == 1:
        View().print_title("Création de JOUEUR")
        player_controller.add_new_player()
        View().print_title("Joueur crée")
    elif input_choice == 2:
        View().print_title("Création de TOURNOI")
        tournament_controller.run_new_tournament(player_controller)
        View().print_title("Tournoi terminé")
    elif input_choice == 0:
        return False
    return True


if __name__ == '__main__':
    while True:
        app = app_running()
        if not app:
            break