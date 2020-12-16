import unittest
from fabonacci import FabNum

class FabTests(unittest.TestCase):
    calc=FabNum()
    def test_simple(self):
        self.assertEqual(self.calc.fab_recursive(10),89)
        self.assertEqual(self.calc.fab_table(5),8)

    def test_stress_test(self):
        for n in range(30):
            self.assertEqual(self.calc.fab_recursive(n),self.calc.fab_table(n))
        
if __name__ == '__main__':
    unittest.main()
