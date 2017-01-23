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

    def test_generate_fibonacci_series_initial(self):
        assert(self.fibonacci_gen.next() == 0)
        assert(self.fibonacci_gen.next() == 1)

    def test_fibonacci_fizzbuzz(self):
        pass

if __name__ == "__main__":
    import nose2
    nose2.main()

