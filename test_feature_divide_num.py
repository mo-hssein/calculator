import unittest
from feature_divide_num import divide


class TestCace(unittest.TestCase):
    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
