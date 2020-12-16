from gcd import GCD
import unittest
class GCDTest(unittest.TestCase):
    calc=GCD()
    def test_simple(self):
        self.assertEqual(self.calc.gcd(105,30),15)
        self.assertEqual(self.calc.gcd(3918848,1653264),61232)
        self.assertEqual(self.calc.gcd_naive(12,4),4)

    def test_stree_test(self):
        for i in range(1,100):
            self.assertEqual(self.calc.gcd(4*i,2*i),self.calc.gcd_naive(4*i,2*i))


if __name__ == '__main__':
    unittest.main()