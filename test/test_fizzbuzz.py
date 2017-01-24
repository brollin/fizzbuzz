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

    def setUp(self):
        self.fibonacci_gen = fizzbuzz.generate_fibonacci_series()
        self.primes_gen = fizzbuzz.generate_prime_number(30)

    def test_convert_to_number(self):
        assert(fizzbuzz.convert_to_number('') is False)
        assert(fizzbuzz.convert_to_number('test') is False)
        assert(fizzbuzz.convert_to_number(10) == 10)
        assert(fizzbuzz.convert_to_number(-10) == -10)
        assert(fizzbuzz.convert_to_number(1.0) == 1)
        assert(fizzbuzz.convert_to_number(1.5) == 1)

    def test_generate_prime_number_initial(self):
        assert(self.primes_gen.next() == 2)
        assert(self.primes_gen.next() == 3)

    def test_generate_prime_number_first10(self):
        assert(self.primes_gen.next() == 2)
        assert(self.primes_gen.next() == 3)
        assert(self.primes_gen.next() == 5)
        assert(self.primes_gen.next() == 7)
        assert(self.primes_gen.next() == 11)
        assert(self.primes_gen.next() == 13)
        assert(self.primes_gen.next() == 17)
        assert(self.primes_gen.next() == 19)
        assert(self.primes_gen.next() == 23)
        assert(self.primes_gen.next() == 29)

    def test_generate_fibonacci_series_initial(self):
        assert(self.fibonacci_gen.next() == 0)
        assert(self.fibonacci_gen.next() == 1)

    def test_generate_fibonacci_series_first10(self):
        assert(self.fibonacci_gen.next() == 0)
        assert(self.fibonacci_gen.next() == 1)
        assert(self.fibonacci_gen.next() == 1)
        assert(self.fibonacci_gen.next() == 2)
        assert(self.fibonacci_gen.next() == 3)
        assert(self.fibonacci_gen.next() == 5)
        assert(self.fibonacci_gen.next() == 8)
        assert(self.fibonacci_gen.next() == 13)
        assert(self.fibonacci_gen.next() == 21)
        assert(self.fibonacci_gen.next() == 34)

    def test_fibonacci_fizzbuzz(self):
        pass


if __name__ == "__main__":
    import nose2
    nose2.main()
