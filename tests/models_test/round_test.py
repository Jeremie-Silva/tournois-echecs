from unittest import TestCase

from app.models.player import Player
from app.models.round import Round


class RoundTestCase(TestCase):

    def setUp(self):
        self.players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        self.round = Round(
            round_name="round_1",
            players_list=self.players_list
        )

    # Round()

    def test_round_is_defined(self):
        self.assertIsInstance(self.round, Round)

    def test_round_attribute_round_name_is_valid(self):
        self.assertEqual(self.round.round_name, "round_1")

    def test_round_attribute_players_list_is_valid(self):
        self.assertEqual(self.round.players_list, self.players_list)
