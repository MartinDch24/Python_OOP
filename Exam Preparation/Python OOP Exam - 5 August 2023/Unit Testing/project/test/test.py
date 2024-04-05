from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Mercedes", "family", 180_000, 10_000)
        self.car_with_repairs = SecondHandCar("Audi", "sports", 10_000, 200_000)
        self.car_with_repairs.repairs.append("Oil change")
        self.car_with_repairs.repairs.append("Tire change")

    def test_correct__init__(self):
        self.assertEqual("Mercedes", self.car.model)
        self.assertEqual("family", self.car.car_type)
        self.assertEqual(180_000, self.car.mileage)
        self.assertEqual(10_000, self.car.price)

    def test_price_getter_and_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_getter_and_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_raises_error_when_setting_a_lower_or_equal_new_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10_000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_returns_string_when_setting_a_higher_price(self):
        result = self.car.set_promotional_price(9_000)

        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(9_000, self.car.price)

    def test_need_repair_when_repair_price_is_higher_than_car_price(self):
        result = self.car.need_repair(6_000, "windshield replacement")

        self.assertEqual('Repair is impossible!', result)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_returns_correct_string_when_repair_is_cheap_enough(self):
        result = self.car.need_repair(5_000, "windshield replacement")

        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(15_000, self.car.price)
        self.assertEqual(["windshield replacement"], self.car.repairs)

    def test_greater_than_dunder_method_with_different_type_cars_returns_a_string(self):
        result = self.car > self.car_with_repairs

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_greater_than_dunder_method_with_same_car_type_compares_prices(self):
        self.car_with_repairs.car_type = "family"
        result = self.car > self.car_with_repairs

        self.assertFalse(result)

    def test__str__method(self):
        result = str(self.car_with_repairs)

        self.assertEqual("""Model Audi | Type sports | Milage 10000km
Current price: 200000.00 | Number of Repairs: 2""", result)


if __name__ == "__main__":
    main()
