import unittest
import regexp_str
regexp_str.check_sentance(regexp_str.my_string)
class TestRegexp_str(unittest.TestCase):

    def test_sentance(self):
        self.assertEqual(regexp_str.my_string, regexp_str.my_string.capitalize())
    def test_sentance_1(self):
        self.assertEqual(regexp_str.my_string[-1], ".")
if __name__ == "__main__":
    unittest.main()
