from unittest import TestCase
from unittest.mock import patch

from app.controllers.round_controller import RoundController
from app.models.match import Match
from app.models.player import Player
from app.models.round import Round
from app.models.tournament import Tournament


class RoundControllerTestCase(TestCase):

    def setUp(self):
        self.round_controller = RoundController()

    # RoundController()

    def test_round_controller_is_defined(self):
        self.assertIsInstance(self.round_controller, RoundController)

    # RoundController.generate_rounds()

    @patch("app.controllers.match_controller.MatchController.retrieve_scores_round")
    @patch("app.controllers.round_controller.RoundController._generate_matchs")
    def test_round_controller_generate_rounds(self, mock_generate_matchs, mock_score):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        tournament = Tournament(
            name="nom du tournoi",
            place="lieu du tournoi",
            date_start="date de début",
            description="description du tournoi",
            number_of_rounds=4,
            players_count=7,
            players_list=players_list
        )
        self.round_controller.generate_rounds(tournament)
        tournament_ready = mock_generate_matchs.call_args_list[-1].args[0]
        self.assertIsInstance(tournament_ready.round_1, Round)
        self.assertIsInstance(tournament_ready.round_2, Round)
        self.assertIsInstance(tournament_ready.round_3, Round)
        self.assertIsInstance(tournament_ready.round_4, Round)
        self.assertEqual(mock_generate_matchs.call_count, tournament.number_of_rounds)
        self.assertEqual(mock_score.call_count, tournament.number_of_rounds)

        self.assertIsInstance(tournament_ready.round_1.date_start, str)
        self.assertIsInstance(tournament_ready.round_1.date_end, str)
        self.assertIsInstance(tournament_ready.round_2.date_start, str)
        self.assertIsInstance(tournament_ready.round_2.date_end, str)
        self.assertIsInstance(tournament_ready.round_3.date_start, str)
        self.assertIsInstance(tournament_ready.round_3.date_end, str)
        self.assertIsInstance(tournament_ready.round_4.date_start, str)
        self.assertIsInstance(tournament_ready.round_4.date_end, str)

    # RoundController._generate_matchs()

    @patch("app.controllers.round_controller.RoundController.get_sorted_players_by_score")
    @patch("app.controllers.round_controller.RoundController.get_last_round")
    def test_round_controller_generate_matchs(self, mock_last_round, mock_sorter):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        tournament = Tournament(
            name="nom du tournoi",
            place="lieu du tournoi",
            date_start="date de début",
            description="description du tournoi",
            number_of_rounds=4,
            players_count=7,
            players_list=players_list
        )
        setattr(tournament, "round_1", Round("round_1", players_list))
        mock_last_round.return_value = getattr(tournament, "round_1")
        self.round_controller._generate_matchs(tournament)
        self.assertIsInstance(tournament.round_1.match_1, Match)
        self.assertIsInstance(tournament.round_1.match_2, Match)
        self.assertIsInstance(tournament.round_1.match_3, Match)
        self.assertEqual(tournament.round_1.waiting_player, players_list[-1])

        tournament.round_1.match_1.score_player_one = 1
        tournament.round_1.match_1.score_player_two = 0
        tournament.round_1.match_2.score_player_one = 0
        tournament.round_1.match_2.score_player_two = 1
        tournament.round_1.match_3.score_player_one = 0.5
        tournament.round_1.match_3.score_player_two = 0.5
        mock_sorter.return_value = [
            tournament.round_1.waiting_player,
            tournament.round_1.match_1.player_one,
            tournament.round_1.match_2.player_two,
            tournament.round_1.match_3.player_one,
            tournament.round_1.match_3.player_two,
            tournament.round_1.match_1.player_two,
            tournament.round_1.match_2.player_one,
        ]
        setattr(tournament, "round_2", Round("round_2", players_list))
        mock_last_round.return_value = getattr(tournament, "round_2")
        self.round_controller._generate_matchs(tournament)
        self.assertIsInstance(tournament.round_2.match_1, Match)
        self.assertIsInstance(tournament.round_2.match_2, Match)
        self.assertIsInstance(tournament.round_2.match_3, Match)
        self.assertEqual(
            tournament.round_2.match_1.player_one,
            tournament.round_1.waiting_player
        )
        self.assertEqual(
            tournament.round_2.match_1.player_two,
            tournament.round_1.match_1.player_one
        )
        self.assertEqual(
            tournament.round_2.match_2.player_one,
            tournament.round_1.match_2.player_two
        )
        self.assertEqual(
            tournament.round_2.match_2.player_two,
            tournament.round_1.match_3.player_one
        )
        self.assertEqual(
            tournament.round_2.match_3.player_one,
            tournament.round_1.match_3.player_two
        )
        self.assertEqual(
            tournament.round_2.match_3.player_two,
            tournament.round_1.match_1.player_two
        )

    # RoundController.get_last_round()

    def test_round_controller_get_last_round(self):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        tournament = Tournament(
            name="nom du tournoi",
            place="lieu du tournoi",
            date_start="date de début",
            description="description du tournoi",
            number_of_rounds=4,
            players_count=7,
            players_list=players_list
        )
        setattr(tournament, "round_1", Round("round_1", players_list))
        setattr(tournament, "round_2", Round("round_2", players_list))
        setattr(tournament, "round_3", Round("round_3", players_list))
        last_round = self.round_controller.get_last_round(tournament)
        self.assertEqual(last_round, tournament.round_3)

    # RoundController.get_sorted_players_by_score()

    def test_round_controller_get_sorted_by_score(self):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
        ]
        tournament = Tournament(
            name="nom du tournoi",
            place="lieu du tournoi",
            date_start="date de début",
            description="description du tournoi",
            number_of_rounds=4,
            players_count=5,
            players_list=players_list
        )
        setattr(tournament, "round_1", Round("round_1", players_list))
        setattr(tournament.round_1, "match_1",
                Match("match_1", tournament.players_list[0], tournament.players_list[1])
        )
        setattr(tournament.round_1, "match_2",
                Match("match_2", tournament.players_list[2], tournament.players_list[3])
        )
        setattr(tournament.round_1, "waiting_player", players_list[-1])
        tournament.round_1.match_1.score_player_one = 1
        tournament.round_1.match_1.score_player_two = 0
        tournament.round_1.match_2.score_player_one = 0.5
        tournament.round_1.match_2.score_player_two = 0.5

        setattr(tournament, "round_2", Round("round_2", players_list))
        sorted_list = self.round_controller.get_sorted_players_by_score(tournament)
        self.assertEqual(sorted_list[0], tournament.players_list[-1])
        self.assertEqual(sorted_list[1], tournament.players_list[0])
        self.assertEqual(sorted_list[2], tournament.players_list[2])
        self.assertEqual(sorted_list[3], tournament.players_list[3])
        self.assertEqual(sorted_list[4], tournament.players_list[1])

        setattr(tournament.round_2, "match_1",
                Match("match_1", sorted_list[0], sorted_list[1])
        )
        setattr(tournament.round_2, "match_2",
                Match("match_2", sorted_list[2], sorted_list[3])
        )
        setattr(tournament.round_2, "waiting_player", sorted_list[-1])
        tournament.round_2.match_1.score_player_one = 0
        tournament.round_2.match_1.score_player_two = 1
        tournament.round_2.match_2.score_player_one = 1
        tournament.round_2.match_2.score_player_two = 0

        setattr(tournament, "round_3", Round("round_3", players_list))
        sorted_list = self.round_controller.get_sorted_players_by_score(tournament)
        self.assertEqual(sorted_list[0], tournament.players_list[1])
        self.assertEqual(sorted_list[1], tournament.players_list[0])
        self.assertEqual(sorted_list[2], tournament.players_list[2])
        self.assertEqual(sorted_list[3], tournament.players_list[3])
        self.assertEqual(sorted_list[4], tournament.players_list[4])
