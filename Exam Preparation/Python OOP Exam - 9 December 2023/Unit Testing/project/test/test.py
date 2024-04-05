from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation("Sofia")

    def test_correct__init__(self):
        self.assertEqual(self.station.name, "Sofia")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_less_than_three_name_chars_raises_error_message(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "So"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_equal_to_three_name_chars_raises_error_message(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "Sof"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_appends_train_info_to_arrival_trains(self):
        self.station.new_arrival_on_board("Sofia-Varna")

        self.assertEqual(self.station.arrival_trains, deque(["Sofia-Varna"]))
        self.assertEqual(self.station.departure_trains, deque())

    def test_train_has_arrived_for_new_train_returns_correct_message(self):
        with self.assertRaises(IndexError) as ie:
            self.station.train_has_arrived("Yambol-Burgas")

        self.station.arrival_trains.append("Sofia-Varna")
        result = self.station.train_has_arrived("Yambol-Burgas")

        self.assertEqual('pop from an empty deque', str(ie.exception))
        self.assertEqual("There are other trains to arrive before Yambol-Burgas.", result)

    def test_train_has_arrived_for_train_to_arrive_returns_correct_message(self):
        self.station.arrival_trains.append("Sofia-Varna")
        result = self.station.train_has_arrived("Sofia-Varna")

        self.assertEqual("Sofia-Varna is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left_returns_true_when_there_are_departure_trains(self):
        self.station.departure_trains = deque(["Sofia-Varna", "Yambol-Burgas", "Sofia-Pleven"])
        result = self.station.train_has_left("Sofia-Varna")

        self.assertTrue(result)
        self.assertEqual(self.station.departure_trains, deque(["Yambol-Burgas", "Sofia-Pleven"]))

    def test_train_has_left_false_when_wrong_departure_train_returns_false(self):
        self.station.departure_trains = deque(["Sofia-Varna", "Yambol-Burgas", "Sofia-Pleven"])
        result = self.station.train_has_left("Yambol-Burgas")

        self.assertFalse(result)


if __name__ == "__main__":
    main()
