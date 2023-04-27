from unittest import TestCase

from app.models.match import Match
from app.models.player import Player


class MatchTestCase(TestCase):

    def setUp(self):
        self.player_one = Player("Clavier", "Christian", "1990-20-10")
        self.player_two = Player("Reno", "Jean", "1990-20-10")
        self.match = Match(
            match_name="match_1",
            player_one=self.player_one,
            player_two=self.player_two
        )

    # Match()

    def test_match_is_defined(self):
        self.assertIsInstance(self.match, Match)

    def test_match_attribute_match_name_is_valid(self):
        self.assertEqual(self.match.match_name, "match_1")

    def test_match_attribute_player_one_is_valid(self):
        self.assertEqual(self.match.player_one, self.player_one)

    def test_match_attribute_player_two_is_valid(self):
        self.assertEqual(self.match.player_two, self.player_two)

    def test_match_attribute_score_player_one_is_valid(self):
        self.assertEqual(self.match.score_player_one, 0)

    def test_match_attribute_score_player_two_is_valid(self):
        self.assertEqual(self.match.score_player_two, 0)
