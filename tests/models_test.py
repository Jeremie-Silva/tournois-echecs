from app.models import (
    Player,
    Tournament,
    Round,
    Match
)
from unittest import TestCase


class PlayerTestCase(TestCase):

    def setUp(self):
        self.player = Player(
            name="Clavier",
            last_name="Christian",
            birth_date="1990-20-10"
        )
        self.custom_player = Player(
            name="Clavier",
            last_name="Christian",
            birth_date="1990-20-10",
            additionnal_one="one",
            additionnal_two="two"
        )

    # Player()

    def test_player_is_defined(self):
        self.assertIsInstance(self.player, Player)

    def test_player_attribute_name_is_valid(self):
        self.assertEqual(self.player.name, "Clavier")

    def test_player_attribute_last_name_is_valid(self):
        self.assertEqual(self.player.last_name, "Christian")

    def test_player_attribute_birth_date_is_valid(self):
        self.assertEqual(self.player.birth_date, "1990-20-10")

    def test_player_attributes_additionals_are_valids(self):
        self.assertEqual(self.custom_player.additionnal_one, "one")
        self.assertEqual(self.custom_player.additionnal_two, "two")

    # Player.__str__()

    def test_player_str_method_is_valid(self):
        self.assertIn(self.player.name, str(self.player))
        self.assertIn(self.player.last_name, str(self.player))
        self.assertIn(self.player.birth_date, str(self.player))


class TournamentTestCase(TestCase):

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
        self.tournament = Tournament(
            name="nom du tournoi",
            place="lieu du tournoi",
            date_start="date de début",
            description="description du tournoi",
            number_of_rounds=4,
            players_count=7,
            players_list=self.players_list
        )

    # Tournament()

    def test_tournament_is_defined(self):
        self.assertIsInstance(self.tournament, Tournament)

    def test_tournament_attribute_name_is_valid(self):
        self.assertEqual(self.tournament.name, "nom du tournoi")

    def test_tournament_attribute_place_is_valid(self):
        self.assertEqual(self.tournament.place, "lieu du tournoi")

    def test_tournament_attribute_date_start_is_valid(self):
        self.assertEqual(self.tournament.date_start, "date de début")

    def test_tournament_attribute_description_is_valid(self):
        self.assertEqual(self.tournament.description, "description du tournoi")

    def test_tournament_attribute_number_of_rounds_is_valid(self):
        self.assertEqual(self.tournament.number_of_rounds, 4)

    def test_tournament_attribute_players_count_is_valid(self):
        self.assertEqual(self.tournament.players_count, 7)

    def test_tournament_attribute_players_list_is_valid(self):
        self.assertEqual(self.tournament.players_list, self.players_list)


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

    # Round._generate_matchs()

    def test_round_generate_matchs_is_valid(self):
        for index in range(len(self.round.players_list)//2):
            curent_match = f"match_{index+1}"
            self.assertIs(type(getattr(self.round, curent_match)), Match)


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
