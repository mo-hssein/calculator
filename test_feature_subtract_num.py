import unittest
from feature_subtract_num import subtract


class TestCace(unittest.TestCase):
    def test_subtract(self):
        result = subtract(10, 1)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
