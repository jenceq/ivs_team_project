""" @package math_lib_tests
    @author: Jan Fiala (xfiala63)
    @brief Documentation for math library tests
"""
import unittest
from math_lib import math_lib 

class Tests(unittest.TestCase):
    """ @brief Tests class to run the tests
        @param unittest.TestCase to access test methods
    """

    def test_add(self):
        """ @brief Method to test addition (x + y)
            @param self Self object
            @returns x + y
        """
        self.assertEqual(math_lib.add(2, 3), 5)
        self.assertEqual(math_lib.add(0, 0), 0)
        self.assertEqual(math_lib.add(2, -3), -1)
        self.assertEqual(math_lib.add(-7467989, -3), -7467992)
        self.assertEqual(math_lib.add(0.155, 0.125), 0.280)
        self.assertEqual(math_lib.add(5000, 15200000), 15205000)
        self.assertEqual(math_lib.add(0, 22.1), 22.1)

    def test_sub(self):
        """ @brief Method to test subtraction (x - y)
            @param self Self object
            @returns x - y
        """
        self.assertEqual(math_lib.sub(2, 3), -1)
        self.assertEqual(math_lib.sub(0, 0), 0)
        self.assertEqual(math_lib.sub(2, -3), 5)
        self.assertEqual(math_lib.sub(-2.15, 3.25), -5.40)
        self.assertEqual(math_lib.sub(777777777, 777777777), 0)



    def test_mul(self):
        """ @brief Method to test multiplication (x * y)
            @param self Self object
            @returns x * y
        """
        self.assertEqual(math_lib.mul(2, 5), 10)
        self.assertEqual(math_lib.mul(512981891981, 0), 0)
        self.assertEqual(math_lib.mul(-10, -10), 100)
        self.assertEqual(math_lib.mul(0.5, 0.5), 0.25)
        self.assertEqual(math_lib.mul(0.1, -0.1), -0.01)
        self.assertEqual(math_lib.mul(-50000000000, -1), 50000000000)


    def test_div(self):
        """ @brief Method to test division (x / y)
            @param self Self object
            @returns x / y
        """
        self.assertRaises(ZeroDivisionError, math_lib.div, 5, 0)
        self.assertEqual(math_lib.div(0, 51485198), 0)
        self.assertEqual(math_lib.div(5, 0.1), 50)
        self.assertEqual(math_lib.div(5, -5), -1)
        self.assertEqual(math_lib.div(5, 5), 1)

    def test_exp(self):
        """ @brief Method to test the exponent (x ^ y) 
            'y' = natural number
            @param self Self object.
            @returns x ^ y
        """
        self.assertEqual(math_lib.exp(5, 2), 25)
        self.assertEqual(math_lib.exp(1, 488548918), 1)
        self.assertEqual(math_lib.exp(-5, 3), -125)
        self.assertRaises(ValueError, math_lib.exp, 5, 2.1)
        self.assertRaises(ValueError, math_lib.exp, 5, -5)
        self.assertEqual(math_lib.exp(-5, 2), 25)

    def test_sqrt(self):
        """ @brief Method to test the square root (sqrt(x, y))
            The value of 'x' has to be >= 0
            The value of 'y' has to be an integer
            @param self Self object
            @returns sqrt(x, y)
        """
        self.assertEqual(math_lib.sqrt(64, 2), 8)
        self.assertRaises(ZeroDivisionError, math_lib.sqrt, 5458489, 0)
        self.assertEqual(math_lib.sqrt(-27, 3), -3)
        self.assertEqual(math_lib.sqrt(1, -2), 1)
        self.assertEqual(math_lib.sqrt(16, 4), 2)
        self.assertEqual(math_lib.sqrt(0, 16), 0)
        self.assertRaises(ValueError, math_lib.sqrt, 0, 0) 

    def test_fact(self):
        """ @brief Method to test the factorial (x!) The value of 'x' has to be a natural number >= 0
            @param self Self object
            @returns x!
        """
        self.assertEqual(math_lib.fact(5), 120)
        self.assertEqual(math_lib.fact(0), 1)
        self.assertEqual(math_lib.fact(2), 2)
        self.assertEqual(math_lib.fact(6), 720)
        self.assertRaises(ValueError, math_lib.fact, -55)
        self.assertRaises(ValueError, math_lib.fact, 1.125)
        self.assertRaises(ValueError, math_lib.fact, -2.54)

if __name__ == '__main__':
    unittest.main()
