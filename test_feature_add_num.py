import unittest
from feature_add_num import add


class TestCace(unittest.TestCase):
    def test_add(self):
        result = add(1, 1)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
