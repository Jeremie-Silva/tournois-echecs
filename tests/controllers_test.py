import datetime
from unittest import TestCase
from unittest.mock import patch, mock_open, MagicMock

from app.controllers import (
	PlayerController, TournamentController, RoundController,
)
from app.models import Player, Tournament
from app.utils import object_to_dict


class PlayerControllerTestCase(TestCase):

	def setUp(self):
		self.player_controller = PlayerController()

	# PlayerController()

	def test_player_controller_is_defined(self):
		self.assertIsInstance(self.player_controller, PlayerController)

	# PlayerController._load_players_from_json()

	@patch("app.controllers.file_opener")
	def test_player_controller_load_players_from_json(self, mock_file_opener):
		test_data = {
			"player_0": {
				"name": "Test Name", "last_name": "Test Last Name", "birth_date": "2000-01-01"
			},
			"player_1": {
				"name": "Test Name", "last_name": "Test Last Name", "birth_date": "2000-01-02", "custom_key": "custom_value"
			}
		}
		mock_file_opener.return_value = test_data
		player_controller = PlayerController()
		self.assertEqual(
			object_to_dict(player_controller.player_0),
			{"name": "Test Name", "last_name": "Test Last Name", "birth_date": "2000-01-01"}
		)
		self.assertEqual(
			object_to_dict(player_controller.player_1),
			{"name": "Test Name", "last_name": "Test Last Name", "birth_date": "2000-01-02", "custom_key": "custom_value"}
		)

	# PlayerController._create_player()

	@patch("app.controllers.PlayerController._load_players_from_json")
	@patch("app.controllers.PlayerController._save_player_to_json")
	@patch("app.views.View.get_information_user")
	def test_player_controller_create_player_from_json(self, mock_get_info, mock_save, mock_load):
		mock_get_info.side_effect = ["name", "last_name", "birth_date"]
		player_controller = PlayerController()
		player_controller.create_player()
		self.assertEqual(mock_get_info.call_count, 3)
		self.assertEqual(type(mock_save.call_args_list[0].args[0]), Player)
		self.assertEqual(mock_load.call_count, 2)

	# PlayerController._save_player_to_json()

	@patch("app.controllers.PlayerController._load_players_from_json")
	@patch("app.controllers.file_writer")
	@patch("app.controllers.file_opener")
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
		mock_custom = mock_open()
		with patch("builtins.open", mock_custom):
			PlayerController()._save_player_to_json(new_player)
		self.assertEqual(mock_file_writer.call_args_list[0].args[1], expected_value)


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

	# TournamentController._load_tournaments_from_json()

	def test_tournament_controller_load_tournaments_from_json(self):
		pass
		# TODO: à faire

	# TournamentController._create_tournament()

	@patch("app.controllers.TournamentController._create_players_list")
	@patch("app.views.View.get_information_user")
	def test_tournament_controller_create_tournament(self, mock_get_info, mock_create_player_list):
		mock_get_info.side_effect = ["nom du tournoi", "lieu du tournoi", "description du tournoi", 3, 6]
		mock_create_player_list.return_value = self.players_list
		result = self.tournament_controller._create_tournament(PlayerController())
		self.assertEqual(type(result), Tournament)

	# TournamentController._create_players_list()

	@patch("app.controllers.PlayerController.create_player")
	@patch("app.views.View.print_players_list")
	@patch("app.controllers.PlayerController._load_players_from_json")
	@patch("app.views.View.get_information_user")
	def test_tournament_controller_create_tournament(self, mock_get_info, mock_player_loader, mock_print_list, mock_create_player):
		player_controller_custom = PlayerController()
		setattr(player_controller_custom, "player_0", Player(name="admin", last_name="admin", birth_date="1111-11-11"))
		setattr(player_controller_custom, "player_1", Player(name="Silva", last_name="Jeremie", birth_date="1111-11-11"))
		setattr(player_controller_custom, "player_2", Player(name="Portugal", last_name="Christopher", birth_date="1111-11-11"))
		setattr(player_controller_custom, "player_3", Player(name="Buret", last_name="Lucy", birth_date="1111-11-11"))
		setattr(player_controller_custom, "player_4", Player(name="Stronkjic", last_name="Sanel", birth_date="1111-11-11"))
		setattr(player_controller_custom, "player_5", Player(name="Alaric", last_name="cybersecu", birth_date="1111-11-11"))
		mock_get_info.side_effect = [0, 1, 2, 3, 4, 0, 5]
		result = self.tournament_controller._create_players_list(5, player_controller_custom)
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

	# TournamentController._generate_matchs()

	def test_tournament_controller_generate_matchs(self):
		pass

	# TournamentController._retrieve_scores()

	def test_tournament_controller_retrieve_scores(self):
		pass
		# TODO: à faire

	# TournamentController.run_new_tournament()

	def test_tournament_controller_run_new_tournament(self):
		pass
		# TODO: à faire

	# TournamentController.save_tournament_to_json()

	def test_tournament_controller_save_tournament_to_json(self):
		pass
		# TODO: à faire


class RoundControllerTestCase(TestCase):

	def setUp(self):
		self.round_controller = RoundController()

	# RoundController()

	def test_round_controller_is_defined(self):
		self.assertIsInstance(self.round_controller, RoundController)

	# RoundController.generate_matchs()

	def test_round_controller_generate_matchs(self):
		pass
		# TODO: reprendre ici

	# RoundController.create_matchs()

	def test_round_controller_create_matchs(self):
		pass
		# TODO: reprendre ici
