import unittest
import regexp_str
regexp_str.check_upercase_and_lowercase(regexp_str.my_string_1)
class TestRegexp_str(unittest.TestCase):

    def test_check_upper_case(self):
        self.assertEqual(regexp_str.my_string_1, regexp_str.my_string_1.capitalize())
    def test_check_number(self):
        self.assertEqual(False, regexp_str.my_string_1.isdigit())

if __name__ == "__main__":
    unittest.main()
