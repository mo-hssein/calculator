import unittest
from feature_multiply_num import multiply


class TestCace(unittest.TestCase):
    def test_multiply(self):
        result = multiply(10, 5)
        self.assertEqual(result, 50)


if __name__ == "__main__":
    unittest.main()
