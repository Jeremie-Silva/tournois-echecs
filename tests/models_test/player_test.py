from unittest import TestCase

from app.models.player import Player


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
