from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")

    def test_correct_init_ignores_non_int_value(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_add_non_int_value_to_the_list(self): # should raise a ValueError
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_int(self): # adds the integer to the list
        expected_list = self.i_list.get_data() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_index_with_out_of_range_index(self): # raises IndexError
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index(self):
        self.i_list.remove_index(1)

        self.assertEqual([1, 3], self.i_list.get_data())

    def test_get_with_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index(self): # should return the value on the index
        result = self.i_list.get(1)
        self.assertEqual(2, result)

    def test_insert_on_invalid_index(self): # should raise IndexError
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_on_valid_index_non_int_type(self): # should raise ValueError
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 6.7)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_on_valid_integer(self):
        expected_list = self.i_list.get_data().copy()

        expected_list.insert(1, 5)
        self.i_list.insert(1, 5)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_get_biggest_number(self):
        result = self.i_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.i_list.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
