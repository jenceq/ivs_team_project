#!/bin/python
"""
@package stddev.py
@author: Patrik Lažek (xlazek01)
@brief math library fucntions
This is the library that reads the data from stdin and calculates the standard deviation to the console 
"""

import sys
from math_lib import math_lib


def file_input():
    """ @brief Function imports data from stdin into list
        @returns numbers - list
    """
    first_line = sys.stdin.readline().strip()

    if ' ' in first_line or '\t' in first_line:
        numbers = first_line.split()
    else:
        numbers = [first_line]
        for line in sys.stdin:
            number = line.strip()
            numbers.append(number)

    return numbers


def remove_white_chars(numbers):
    """ 
    @brief Function removes white chars from list
    @param numbers - list
    """
    index_to_delete = []
    for i in range(0, len(numbers)):
        if numbers[i] == '':
            index_to_delete.append(i)
    num_of_deletions = 0
    for index in index_to_delete:
        index -= num_of_deletions
        del numbers[index]
        num_of_deletions += 1


def format_floats(numbers):
    """ 
    @brief Function replaces ',' with '.' and converts value into float
    @param numbers - list
    """
    for i, number in enumerate(numbers):
        if '.' in number:
            numbers[i] = float(number)
        elif ',' in number:
            numbers[i] = number.replace(",", ".")
            numbers[i] = float(numbers[i])
        else:
            numbers[i] = int(number)

#1.470 seconds
def standart_deviation(data):
    """
    @brief Function that evaluates standart deviation from dataset
    @param data - list
    @returns standart deviation
    """
    diff_squared = []
    sum = 0
    sum_of_diff = 0
    n = len(data)

    if n == 1:
        raise ValueError("Not enough data.")

    for number in data:
        sum = math_lib.add(sum, number)

    average = math_lib.div(sum, n)

    for i in range(n):
        diff_squared.append(math_lib.exp(math_lib.sub(data[i], average), 2))

    for number in diff_squared:
        sum_of_diff = math_lib.add(sum_of_diff, number)
    
    return math_lib.sqrt(math_lib.div(sum_of_diff, n-1), 2)


data = file_input()
remove_white_chars(data)
format_floats(data)
print(standart_deviation(data))