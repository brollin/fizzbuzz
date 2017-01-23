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

def convert_to_number(string):
    """
    Tries to cast input into an integer number, returning the
    number if successful and returning False otherwise.
    """
    try:
        number = int(string)
        return number
    except:
        return False


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


if __name__ == "__main__":
    """
    Welcome user and ask for a number of output lines. Run
    fibonacci_fizzbuzz with this amount of output lines.
    """
    welcome_text = 'Welcome to Fibonacci FizzBuzz!'
    input_text = 'How many lines of output? Enter a positive number:'
    invalid_input = 'Error - input was not a positive number.\n'

    # Attempt to obtain a valid number of output lines from the user
    output_count = convert_to_number(input(input_text))
    while not output_count or output_count < 0:
        output_count = convert_to_number(input(invalid_input + input_text))

    print 'Running Fibonacci FizzBuzz with', output_count, 'lines of output...'

    fibonacci_fizzbuzz(output_count)
