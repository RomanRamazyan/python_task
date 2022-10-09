import regexp_str
import unittest
regexp_str.natural_number(regexp_str.my_string_2)

class TestRegexp_str(unittest.TestCase):

    def test_natural_numbers(self):
        self.assertEqual(True, regexp_str.my_string_2.isdigit())
        if self.assertLessEqual(int(regexp_str.my_string_2), 9):
            self.assertIsNot(regexp_str.my_string_2, "natural number")

if __name__ == "__main__":
    unittest.main()
