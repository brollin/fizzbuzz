#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fizzbuzz.py
~~~~~~~~~~~

A module for generating the first n Fibonacci
numbers as F(n), displaying:
\n- "Buzz" when F(n) is divisible by 3,
\n- "Fizz" when F(n) is divisible by 5,
\n- "FizzBuzz" when F(n) is divisible by 15,
\n- "BuzzFizz" when F(n) is prime,
\n- the value F(n) otherwise.

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


def generate_prime_number(count=20):
    """
    Returns a generator function for prime numbers,
    utilizing the Sieve of Eratosthenes.

    count -- number that primes are considered up to using
                Erastosthenes Sieve. Generator performs slowly
                after this number.
    """
    if count <= 1:
        yield 1
        return

    # Initialize an array to track whether each digit is prime
    primes_tracker = [True] * count
    primes_tracker[0] = primes_tracker[1] = False

    # Loop through the primes_tracker, yielding numbers that are prime
    for number, is_prime in enumerate(primes_tracker):
        if is_prime:
            yield number

            # Mark future multiples of this prime as not prime
            for index in xrange(number*number, count, number):
                primes_tracker[index] = False

    # Resort to slower prime checking algorithm
    number = count
    while True:
        found = True
        for divider in xrange(2, int(number**0.5)+1):
            if number % divider == 0:
                found = False
        if found:
            yield number

        number += 1


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
        # Yield a number that is the sum of the previous two numbers.
        x, y = y, x + y
        yield y


def fibonacci_fizzbuzz(output_count=20):
    """
    Prints a Fibonacci series F(n), displaying:
      - "Buzz" when F(n) is divisible by 3,\n
      - "Fizz" when F(n) is divisible by 5,\n
      - "FizzBuzz" when F(n) is divisible by 15,\n
      - "BuzzFizz" when F(n) is prime,\n
      - the value F(n) otherwise.

    output_count -- number of lines of output (default 20)
    """
    # Find the n-th Fibonacci number with Binet's Formula
    golden = (5**0.5 + 1) / 2
    nth_fibonacci = int(round((golden**output_count) / (5**0.5)))

    # Create a prime number generator
    primes_gen = generate_prime_number(nth_fibonacci)

    # Create a fibonacci series generator
    fibonacci_gen = generate_fibonacci_series()

    # Loop until the number of desired output lines
    output = 0
    next_prime = primes_gen.next()
    while output < output_count:
        next_output = fibonacci_gen.next()

        if next_output > next_prime:
            while next_output > next_prime:
                next_prime = primes_gen.next()
        if next_output == next_prime:
            next_output = 'BuzzFizz'
            if output + 1 < output_count:
                next_prime = primes_gen.next()

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


if __name__ == "__main__":
    """
    Welcomes user and asks for a number of output lines. Runs
    fibonacci_fizzbuzz with this amount of output lines.
    """

    # Configure an argument parser
    import argparse
    parser = argparse.ArgumentParser(description='Apply Fizzbuzz to a Fibonacci series.')
    args = parser.parse_args()

    welcome_text = 'Welcome to Fibonacci FizzBuzz!'
    input_text = 'How many lines of output? Enter a number between 1 and 40:\n'
    invalid_input = 'Error - input was not in the proper range.\n'

    print '-'*30
    print welcome_text
    print '-'*30

    # Attempt to obtain a valid number of output lines from the user
    output_count = convert_to_number(raw_input(input_text))
    while not output_count or output_count < 1 or output_count > 40:
        output_count = convert_to_number(raw_input(invalid_input + input_text))

    print 'Running Fibonacci FizzBuzz with', output_count, 'lines of output...'
    print '-'*30

    # Run Fibonacci Fizzbuzz and report the runtime
    import time
    start = time.time()
    fibonacci_fizzbuzz(output_count)
    end = time.time() - start
    print '-'*30
    print 'Runtime was %s seconds.' % end
