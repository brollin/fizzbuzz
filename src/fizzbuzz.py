#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    fizzbuzz.py

    A module for generating the first n Fibonacci
    numbers as F(n), displaying:
        "Buzz" when F(n) is divisible by 3,
        "Fizz" when F(n) is divisible by 5,
        "FizzBuzz" when F(n) is divisible by 15,
        "BuzzFizz" when F(n) is prime,
        the value F(n) otherwise.

"""


def fibonacci_fizzbuzz(output=100):
    """
    Print a Fibonacci series F(n), displaying:
        "Buzz" when F(n) is divisible by 3,
        "Fizz" when F(n) is divisible by 5,
        "FizzBuzz" when F(n) is divisible by 15,
        "BuzzFizz" when F(n) is prime,
        the value F(n) otherwise.

    output -- number of lines of output (default 100)
    """
    pass


def generate_fibonacci_series():
    """
    Generator function for a Fibonacci series.
    """

    # Initially yield a 0 and 1 to start the series
    x = 0
    yield x
    y = 1
    yield y

    while True:
        # Yield a number that is the sum of the previous
        #   two numbers.
        x, y = y, x + y
        yield y


def dynamic_fibonacci(fib_series, memo):
    """
    Generate the next number in the Fibonacci series.

    fib_series -- list of Fibonacci series so far
    memo -- memoization of previous Fib
    """
    pass


if __name__ == "__main__":
    print "Welcome to FizzBuzz."

    fibonacci_fizzbuzz()
