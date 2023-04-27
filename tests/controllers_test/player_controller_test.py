from unittest import TestCase
from unittest.mock import patch

from app.controllers.player_controller import PlayerController
from app.models.player import Player


class PlayerControllerTestCase(TestCase):

    # PlayerController._load_players_from_json()

    @patch("app.controllers.player_controller.file_opener")
    def test_player_controller_load_players_from_json(self, mock_file_opener):
        test_data = {
            "player_0": {
                "name": "Garcia", "last_name": "José", "birth_date": "2000-01-01"
            },
            "player_1": {
                "name": "Solo", "last_name": "Bruno", "birth_date": "2000-01-02", "custom_key": "custom_value"
            }
        }
        mock_file_opener.return_value = test_data
        player_controller = PlayerController()

        self.assertEqual(player_controller.player_0.name, "Garcia",)
        self.assertEqual(player_controller.player_0.last_name, "José",)
        self.assertEqual(player_controller.player_0.birth_date, "2000-01-01",)

        self.assertEqual(player_controller.player_1.name, "Solo",)
        self.assertEqual(player_controller.player_1.last_name, "Bruno",)
        self.assertEqual(player_controller.player_1.birth_date, "2000-01-02",)
        self.assertEqual(player_controller.player_1.custom_key, "custom_value",)

    # PlayerController._create_player()

    @patch("app.controllers.player_controller.PlayerController._load_players_from_json")
    @patch("app.controllers.player_controller.PlayerController._save_player_to_json")
    @patch("app.views.main_view.MainView.get_information_user")
    def test_player_controller_create_player_from_json(self, mock_get_info, mock_save, mock_load):
        mock_get_info.side_effect = ["name", "last_name", "birth_date"]
        PlayerController().create_player()
        self.assertEqual(mock_get_info.call_count, 3)
        self.assertIsInstance(mock_save.call_args_list[0].args[0], Player)
        self.assertEqual(mock_load.call_count, 2)

    # PlayerController._save_player_to_json()

    @patch("app.controllers.player_controller.PlayerController._load_players_from_json")
    @patch("app.controllers.player_controller.file_writer")
    @patch("app.controllers.player_controller.file_opener")
    def test_player_controller_save_player_to_json(self, mock_file_opener, mock_file_writer, mock_load):
        data = {
            "player_0": {"birth_date": "1111-11-11", "last_name": "admin", "name": "admin"},
            "player_1": {"birth_date": "1993-03-28", "last_name": "Jeremie", "name": "Silva"},
            "player_2": {"birth_date": "1992-05-19", "last_name": "Christopher", "name": "Portugal"},
            "player_3": {"birth_date": "1991-08-31", "last_name": "Lucy", "name": "Buret"},
        }
        new_player = Player(
            name="Clavier",
            last_name="Christian",
            birth_date="1990-20-10"
        )
        expected_value = {
            "player_0": {"birth_date": "1111-11-11", "last_name": "admin", "name": "admin"},
            "player_1": {"birth_date": "1993-03-28", "last_name": "Jeremie", "name": "Silva"},
            "player_2": {"birth_date": "1992-05-19", "last_name": "Christopher", "name": "Portugal"},
            "player_3": {"birth_date": "1991-08-31", "last_name": "Lucy", "name": "Buret"},
            "player_4": {"birth_date": "1990-20-10", "last_name": "Christian", "name": "Clavier"},
        }
        mock_file_opener.return_value = data
        PlayerController()._save_player_to_json(new_player)
        mock_file_opener.assert_called_once_with("players")
        mock_file_writer.assert_called_once_with("players", expected_value)
