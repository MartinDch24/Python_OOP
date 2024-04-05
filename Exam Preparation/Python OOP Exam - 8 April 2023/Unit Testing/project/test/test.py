from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Ben", 18, 3)
        self.opponent = TennisPlayer("Zack", 21, 4)

    def test_correct__init__(self):
        self.assertEqual("Ben", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(3, self.player.points)

    def test_name_getter_and_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "ab"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_getter_and_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_success(self):
        self.player.add_new_win("new_tournament")
        self.player.add_new_win("another_tournament")

        self.assertEqual(["new_tournament", "another_tournament"], self.player.wins)

    def test_add_new_win_failure_should_return_a_string(self):
        self.player.add_new_win("new_tournament")
        result = self.player.add_new_win("new_tournament")

        self.assertEqual("new_tournament has been already added to the list of wins!", result)

    def test_lower_than_dunder_method(self):
        result = self.player < self.opponent
        second_result = self.opponent < self.player

        self.assertEqual('Zack is a top seeded player and he/she is better than Ben', result)
        self.assertEqual('Zack is a better player than Ben', second_result)

    def test_string_representation_of_an_instance_of_the_class(self):
        self.player.wins = ["tournament1", "tournament2", "tournament3"]
        result = str(self.player)

        self.assertEqual("Tennis Player: Ben\nAge: 18\nPoints: 3.0\nTournaments won: tournament1, tournament2, tournament3", result)


if __name__ == "__main__":
    main()
