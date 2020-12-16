import unittest
from random import randint
from max_pairs import MaxPairs


class MaxPairsTest(unittest.TestCase):
    calc=MaxPairs()
    max_size= 2 * 10 ** 3
    def test_simple(self):
        self.assertEqual(self.calc.max_pairs([1,2,3]),6)
        self.assertEqual(self.calc.max_pairs([1,2,8]),16)
        self.assertEqual(self.calc.max_pairs([1,2,33]),66)

    def test_stree_test(self):
        """
        stree test compare two alogrithms result with a large set
        """
        for _ in range(10):
            rand_numbers = [randint(0,self.max_size) for _ in range(0, self.max_size)]
            result = self.calc.max_pairs(rand_numbers)
            result2= self.calc.max_pairs_naive(rand_numbers)
            print(result,result2)
            self.assertEqual(result, result2)
    def test_big_set(self):
        """
        assert edge case
        """
        max_value= 2 * 10**5
        rand_numbers = list(range(0, max_value))
        result = self.calc.max_pairs(rand_numbers)
        self.assertGreater(result,5000000)

if __name__ == "__main__":
    unittest.main()
