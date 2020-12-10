import unittest
from week01.max_pairs import MaxPairs


class MaxPairsTest(unittest.TestCase):
    def test_by_range(self):
        rand_numbers = [n for n in range(0, 1000)]
        result = MaxPairs().calc_max_pairs(rand_numbers)
        print(result)
        self.assertGreaterEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
