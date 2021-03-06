# fizzbuzz

## Overview

Performs FizzBuzz on a Fibonacci series by displaying:
- "Buzz" when F(n) is divisible by 3,
- "Fizz" when F(n) is divisible by 5,
- "FizzBuzz" when F(n) is divisible by 15,
- "BuzzFizz" when F(n) is prime, or
- the value F(n) otherwise.

The number of lines of output is determined by the user.

## Installation

To install, clone the GitHub repository and inside the top-level repository directory run:
```
$ make init
```
> Note: it may be necessary to ```sudo make init``` if permission errors occur.

To run:
```
$ python fizzbuzz/fizzbuzz.py
```

To run the nose2 tests:
```
$ make test
```

To generate the documenation:
```
$ cd docs
$ make html
```
The documentation can be viewed at ```docs/_build/html/index.html```, relative the top-level repo directory.

## Constraints

Depending on the memory of your system, it may not be possible to compute the full 40 lines of output.
