from controllers import (
    TournamentController
)
from views import View


if __name__ == '__main__':
    tournament_controller = TournamentController()
    # input_choice = View().main_menu()
    input_choice = 1
    if input_choice == 1:
        tournament_controller.run_new_tournament()
