from unittest import TestCase

from app.models.player import Player
from app.models.tournament import Tournament


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
