from unittest import TestCase
from unittest.mock import patch

from app.controllers.match_controller import MatchController
from app.models.match import Match
from app.models.player import Player
from app.models.round import Round


class MatchControllerTestCase(TestCase):

    def setUp(self):
        self.match_controller = MatchController()

    # MatchController()

    def test_match_controller_is_defined(self):
        self.assertIsInstance(self.match_controller, MatchController)

    # MatchController.retrieve_scores_round()

    @patch("app.views.main_view.MainView.get_result_match")
    def test_match_controller_retrieve_scores_round(self, mock_get_result):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        round_1 = Round("round_1", players_list)
        setattr(round_1, "match_1",	Match("match_1", players_list[0], players_list[1]))
        setattr(round_1, "match_2",	Match("match_2", players_list[2], players_list[3]))
        setattr(round_1, "match_3",	Match("match_3", players_list[4], players_list[5]))
        mock_get_result.side_effect = ["joueur 1", "joueur 2", "autre"]
        self.match_controller.retrieve_scores_round(round_1)
        self.assertEqual(round_1.match_1.score_player_one, 1)
        self.assertEqual(round_1.match_1.score_player_two, 0)
        self.assertEqual(round_1.match_2.score_player_one, 0)
        self.assertEqual(round_1.match_2.score_player_two, 1)
        self.assertEqual(round_1.match_3.score_player_one, 0.5)
        self.assertEqual(round_1.match_3.score_player_two, 0.5)
