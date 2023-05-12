from unittest import TestCase
from unittest.mock import patch

from app.controllers.player_controller import PlayerController
from app.controllers.tournament_controller import TournamentController
from app.models.player import Player
from app.models.tournament import Tournament
from app.utils import object_to_dict


class TournamentControllerTestCase(TestCase):

    def setUp(self):
        self.tournament_controller = TournamentController()
        self.players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]

    # TournamentController()

    def test_tournament_controller_is_defined(self):
        self.assertIsInstance(self.tournament_controller, TournamentController)

    # TournamentController.create_tournament()

    @patch("app.controllers.player_controller.PlayerController.load_players_from_json")
    @patch("app.controllers.tournament_controller.TournamentController.create_players_list")
    @patch("app.views.main_view.MainView.get_information_user")
    def test_tournament_controller_create_tournament(self, mock_get_info, mock_create_player_list, mock_load_player):
        mock_get_info.side_effect = ["nom du tournoi", "lieu du tournoi", "description du tournoi", 3, 6]
        mock_create_player_list.return_value = self.players_list
        result = TournamentController().create_tournament(PlayerController())
        self.assertIsInstance(result, Tournament)

    # TournamentController.create_players_list()

    @patch("app.controllers.player_controller.PlayerController.create_player")
    @patch("app.views.main_view.MainView.print_players_list")
    @patch("app.controllers.player_controller.PlayerController.load_players_from_json")
    @patch("app.views.main_view.MainView.get_information_user")
    def test_tournament_controller_create_players_list(self, mock_get_info, mock_player_loader, mock_print_list, mock_create_player):
        player_controller_custom = PlayerController()
        setattr(player_controller_custom, "player_0", Player(name="admin", last_name="admin", birth_date="1111-11-11"))
        setattr(player_controller_custom, "player_1", Player(name="Silva", last_name="Jeremie", birth_date="1111-11-11"))
        setattr(player_controller_custom, "player_2", Player(name="Portugal", last_name="Christopher", birth_date="1111-11-11"))
        setattr(player_controller_custom, "player_3", Player(name="Buret", last_name="Lucy", birth_date="1111-11-11"))
        setattr(player_controller_custom, "player_4", Player(name="Stronkjic", last_name="Sanel", birth_date="1111-11-11"))
        setattr(player_controller_custom, "player_5", Player(name="Alaric", last_name="cybersecu", birth_date="1111-11-11"))
        mock_get_info.side_effect = [0, 1, 2, 3, 4, 0, 5]
        result = self.tournament_controller.create_players_list(5, player_controller_custom)
        self.assertEqual(
            object_to_dict(result),
            [{'birth_date': '1111-11-11', 'last_name': 'Jeremie', 'name': 'Silva'},
             {'birth_date': '1111-11-11', 'last_name': 'Christopher', 'name': 'Portugal'},
             {'birth_date': '1111-11-11', 'last_name': 'Lucy', 'name': 'Buret'},
             {'birth_date': '1111-11-11', 'last_name': 'Sanel', 'name': 'Stronkjic'},
             {'birth_date': '1111-11-11', 'last_name': 'cybersecu', 'name': 'Alaric'}]
        )
        self.assertEqual(mock_create_player.call_count, 2)
        self.assertEqual(mock_print_list.call_count, 3)

    # TournamentController.run_new_tournament()

    def test_tournament_controller_run_new_tournament(self):
        pass

    # TournamentController.save_tournament_to_json()

    def test_tournament_controller_save_tournament_to_json(self):
        pass
