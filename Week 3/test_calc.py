import unittest
import calc

class TestMath(unittest.TestCase):
    def setUp(self):
        pass
    def test_add_10_5(self):
        self.assertEqual(calc.add(-10,-5),-15)
    def test_subtract_10_5(self):
        self.assertEqual(calc.subtract(10,5),5)
    def test_multiply_10_5(self):
        self.assertEqual(calc.multiply(-10,5),-50)
    def test_divide_10_5(self):
        self.assertEqual(calc.divide(10,5),2.0) #Test divide by 0 case
        with self.assertRaises(ValueError):calc.divide(1,0)
if __name__=='__main__':
    unittest.main()
