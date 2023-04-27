import json
from unittest import TestCase
from unittest.mock import patch, mock_open, call

from app.models.round import Round
from app.utils import object_to_dict, file_opener, file_writer
from app.models.match import Match
from app.models.player import Player
from app.models.tournament import Tournament
from app.models.match import Match


class UtilsTestCase(TestCase):

    # utils.file_opener()

    def test_utils_file_opener_is_valid(self):
        mock_data = {"data": "mocked"}
        mock = mock_open(read_data=json.dumps(mock_data))
        with patch("builtins.open", mock):
            result = file_opener("my_file")
        self.assertEqual(result, mock_data)
        mock.assert_called_once_with('Data/my_file.json', 'r')

    # utils.file_writer()

    def test_utils_file_writer_is_valid(self):
        data = {"data": "test"}
        mock_custom = mock_open()
        with patch("builtins.open", mock_custom):
            file_writer("my_file", data)
        mock_custom.assert_called_once_with('Data/my_file.json', 'w')
        expected_calls = [call("{"), call('"data"'), call(': '), call('"test"'), call("}")]
        mock_custom().write.assert_has_calls(expected_calls)

    # utils.object_to_dict() -> Player

    def test_utils_object_to_dict_for_player(self):
        player = Player(
            name="Clavier",
            last_name="Christian",
            birth_date="1990-20-10"
        )
        expected_output_player_dict = {
            "name": "Clavier",
            "last_name": "Christian",
            "birth_date": "1990-20-10"
        }
        self.assertEqual(
            object_to_dict(player),
            expected_output_player_dict
        )

    # utils.object_to_dict() -> Tournament

    def test_utils_object_to_dict_for_tournament(self):
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
        expected_output_tournament_dict = {
            "name": "nom du tournoi",
            "place": "lieu du tournoi",
            "date_start": "date de début",
            "description": "description du tournoi",
            "number_of_rounds": 4,
            "players_count": 7,
            "players_list": [
                {
                    "name": "Clavier",
                    "last_name": "Christian",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Reno",
                    "last_name": "Jean",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Astier",
                    "last_name": "Alexandre",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Naseri",
                    "last_name": "Sami",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Solo",
                    "last_name": "Bruno",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Le Bolloc'h",
                    "last_name": "Yvan",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Garcia",
                    "last_name": "José",
                    "birth_date": "1990-20-10"
                }
            ]
        }
        self.assertEqual(
            object_to_dict(tournament),
            expected_output_tournament_dict
        )

    # utils.object_to_dict() -> Round

    def test_utils_object_to_dict_for_round(self):
        players_list = [
            Player("Clavier", "Christian", "1990-20-10"),
            Player("Reno", "Jean", "1990-20-10"),
            Player("Astier", "Alexandre", "1990-20-10"),
            Player("Naseri", "Sami", "1990-20-10"),
            Player("Solo", "Bruno", "1990-20-10"),
            Player("Le Bolloc'h", "Yvan", "1990-20-10"),
            Player("Garcia", "José", "1990-20-10"),
        ]
        expected_output_round_dict = {
            "players_list": [
                {
                    "name": "Clavier",
                    "last_name": "Christian",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Reno",
                    "last_name": "Jean",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Astier",
                    "last_name": "Alexandre",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Naseri",
                    "last_name": "Sami",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Solo",
                    "last_name": "Bruno",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Le Bolloc'h",
                    "last_name": "Yvan",
                    "birth_date": "1990-20-10"
                },
                {
                    "name": "Garcia",
                    "last_name": "José",
                    "birth_date": "1990-20-10"
                }
            ],
            "round_name": "round_1"
        }
        round = Round(
            round_name="round_1",
            players_list=players_list
        )
        self.assertEqual(
            object_to_dict(round),
            expected_output_round_dict
        )

    # utils.object_to_dict() -> Match

    def test_utils_object_to_dict_for_match(self):
        player_one = Player("Clavier", "Christian", "1990-20-10")
        player_two = Player("Reno", "Jean", "1990-20-10")
        match = Match(
            match_name="match_1",
            player_one=player_one,
            player_two=player_two
        )
        expected_output_match_dict = {
            "match_name": "match_1",
            "player_one": {
                "name": "Clavier",
                "last_name": "Christian",
                "birth_date": "1990-20-10"
            },
            "player_two": {
                "name": "Reno",
                "last_name": "Jean",
                "birth_date": "1990-20-10"
            },
            "score_player_one": 0,
            "score_player_two": 0
        }
        self.assertEqual(
            object_to_dict(match),
            expected_output_match_dict
        )
