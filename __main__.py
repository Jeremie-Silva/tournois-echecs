from controllers import (
    TournamentController,
    PlayerController
)
from views import View


def app_launcher():
    player_controller = PlayerController()
    player_controller.instantiate_players_from_json()
    tournament_controller = TournamentController()
    # input_choice = View().main_menu()
    input_choice = 2
    if input_choice == 1:
        player_controller.add_new_player()
    elif input_choice == 2:
        tournament_controller.run_new_tournament(player_controller)


if __name__ == '__main__':
    app_launcher()
