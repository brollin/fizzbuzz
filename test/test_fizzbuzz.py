#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_fizzbuzz.py

    A module for testing features of the fizzbuzz
    package.
"""

import unittest
import fizzbuzz


class FizzBuzzTestSuite(unittest.TestCase):
    """
    TODO
    """

    def setUp(self):
        self.fibonacci_gen = fizzbuzz.generate_fibonacci_series()

    def test_convert_to_number(self):
        assert(fizzbuzz.convert_to_number('') == False)
        assert(fizzbuzz.convert_to_number('test') == False)
        assert(fizzbuzz.convert_to_number(10) == 10)
        assert(fizzbuzz.convert_to_number(-10) == -10)
        assert(fizzbuzz.convert_to_number(1.0) == 1)
        assert(fizzbuzz.convert_to_number(1.5) == 1)
        
    def test_generate_fibonacci_series_initial(self):
        assert(self.fibonacci_gen.next() == 0)
        assert(self.fibonacci_gen.next() == 1)

    def test_fibonacci_fizzbuzz(self):
        pass


if __name__ == "__main__":
    import nose2
    nose2.main()
