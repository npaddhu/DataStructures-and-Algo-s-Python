"""Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
The random module includes a more basic function randrange, with parameterization similar to the built-in range
function, that return a random choice from the given range. Using only the randrange function, implement your own
version of the choice function.
"""

import random


def rand_number():
    # equal to choice([100, 105, 110, ..... 195])
    return random.randrange(100, 200, 5)


if __name__ == '__main__':
    print(rand_number())