import unittest
from src.calculator import calc

class Test_Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,2),3)

    def test_sub(self):
        self.assertEqual(calc.subtract(2,3),-1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(18,3),6)
        self.assertRaises(calc.DivisionError,calc.divide,18,0)

# $ python -m unittest unittests.test_calc
