from app.controllers.tournament_controller import TournamentController
from app.controllers.player_controller import PlayerController
from app.views.flask_view import FlaskView
from app.views.main_view import MainView


def app_running():
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    input_choice = MainView().main_menu()
    input_choice = 3
    if input_choice == 1:
        MainView().print_title("Création de JOUEUR")
        player_controller.create_player()
        MainView().print_title("Joueur crée")
    elif input_choice == 2:
        MainView().print_title("Création de TOURNOI")
        tournament_controller.run_new_tournament(player_controller)
        MainView().print_title("Tournoi terminé")
    elif input_choice == 3:
        FlaskView("tournament_matchs_list", tournament_selected="Championnat de France")
    elif input_choice == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    while True:
        app = app_running()
        if not app:
            break
