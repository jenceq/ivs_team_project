#!/bin/python
"""
@package math_lib
@author: Patrik Lažek (xlazek01)
@brief math library fucntions
This is a simple math library that provides various mathematical functions, such as addition, subtraction,
multiplication, division, exponentiation, factorial, and nth root calculation. All functions are static methods
and can be called directly from the math_lib module.

Supported functions:
    - add(x, y)
    - sub(x, y)
    - mul(x, y)
    - div(x, y)
    - exp(x, n)
    - fact(n)
    - sqrt(x, n)
"""

class math_lib:

    @staticmethod
    def add(x, y):
        """
        Adds two numbers and returns the result.

        param x: The first number to be added.
        param y: The second number to be added.
        return: The sum of two numbers.
        """
        return x + y
    
    @staticmethod
    def sub(x, y):
        """
        Subtracts y from x and returns the result.

        param x: The number to be subtracted from.
        param y: The number to subtract.
        return: The difference between x and y.
        """
        return x - y
    
    @staticmethod
    def mul(x, y):
        """
        Multiplies two numbers and returns the result.

        param x: The first number to be multiplied.
        param y: The second number to be multiplied.
        return: The product of x and y.
        """
        return round(x * y, 12)
    
    @staticmethod
    def div(x, y):
        """
        Divides x by y and returns the result as a float.

        param x: The numerator.
        param y: The denominator. Must not be zero.
        return: The result of the division as a float.
        raises ValueError: If the denominator is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Zero div Error")
        x = float(x)
        return round(x / y, 12)
    
    @staticmethod
    def fact(n):
        """
        Calculates the factorial of a non-negative integer n and returns the result.

        param n: The number to calculate the factorial of.
        return: The factorial of n.
        raises ValueError: If n is negative or not an integer.
        """
        if type(n) != int or n < 0:
            raise ValueError("Math Error")
        if n == 0:
            return 1
        else:
            return n * math_lib.fact(n-1)
    
    @staticmethod
    def exp(x, n):
        """
        Raises a number x to the power of a non-zero positive integer n and returns the result.

        param x: The base number to raise to a power.
        param n: The positive integer power to raise x to.
        return: The result of raising x to the power of n.
        raises ValueError: If n is not a positive integer.
        """
        if type(n) != int or n <= 0:
            raise ValueError("Math Error")
        return x ** n
    
    @staticmethod
    def sqrt(x, n):
        """
        Calculates the nth root of a non-negative number x and returns the result.

        param x: The non-negative number to calculate the nth root of.
        param n: The positive integer root to calculate.
        return: The result of taking the nth root of x.
        raises ValueError: If x is negative or n is not a positive integer.
        """
        if n == 0:
            raise ZeroDivisionError("Zero div Error")
        if x < 0 and n % 2 == 0:
            raise ValueError("Math Error")
        return x ** (1/n)