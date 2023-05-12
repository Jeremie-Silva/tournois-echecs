from app.controllers.tournament_controller import TournamentController
from app.controllers.player_controller import PlayerController
from app.views.flask_view import FlaskView
from app.views.main_view import MainView


def app_running() -> bool:
    """The function is called without parameters at the start of the application,
    initializes the player controller and the tournament controller, and launches the user menu.
    If it returns true the application restarts, if it returns false the application shuts down"""
    player_controller: object = PlayerController()
    tournament_controller: object = TournamentController()
    input_choice: int = MainView().main_menu()
    if input_choice == 1:
        MainView().print_title("Création de JOUEUR")
        player_controller.create_player()
        MainView().print_title("Joueur crée")
    elif input_choice == 2:
        MainView().print_title("Création de TOURNOI")
        tournament_controller.run_new_tournament(player_controller)
        MainView().print_title("Tournoi terminé")
    elif input_choice == 3:
        expected_report, tournament_name = MainView().report_menu()
        FlaskView(expected_report, tournament_selected=tournament_name)
    elif input_choice == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    while True:
        app: bool = app_running()
        if not app:
            break
