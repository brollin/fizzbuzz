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


def fibonacci_fizzbuzz(output_count=100):
    """
    Prints a Fibonacci series F(n), displaying:
        "Buzz" when F(n) is divisible by 3,
        "Fizz" when F(n) is divisible by 5,
        "FizzBuzz" when F(n) is divisible by 15,
        "BuzzFizz" when F(n) is prime,
        the value F(n) otherwise.

    output_count -- number of lines of output (default 100)
    """

    # Create a fibonacci series generator
    fibonacci_gen = generate_fibonacci_series()

    # Loop until the number of desired output lines
    output = 0
    while output <= output_count:
        next_output = fibonacci_gen.next()

        if is_prime(next_output):
            next_output = 'BuzzFizz'

        else:
            # Depending on divisibility, modify
            # the output string
            out = ''
            if next_output % 5 == 0:
                out += 'Fizz'
            if next_output % 3 == 0:
                out += 'Buzz'
            if not out:
                out = next_output

        print next_output
        output += 1


def is_prime(number):
    """
    Returns True if input is prime, otherwise False.
    """
    return False


def generate_fibonacci_series():
    """
    Returns generator function for a Fibonacci series.
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
    Welcomes user and asks for a number of output lines. Runs
    fibonacci_fizzbuzz with this amount of output lines.
    """
    welcome_text = 'Welcome to Fibonacci FizzBuzz!'
    input_text = 'How many lines of output? Enter a positive number:\n'
    invalid_input = 'Error - input was not a positive number.\n'

    print '-'*30
    print welcome_text
    print '-'*30

    # Attempt to obtain a valid number of output lines from the user
    output_count = convert_to_number(input(input_text))
    while not output_count or output_count < 0:
        output_count = convert_to_number(input(invalid_input + input_text))

    print 'Running Fibonacci FizzBuzz with', output_count, 'lines of output...'
    print '-'*30

    fibonacci_fizzbuzz(output_count)
