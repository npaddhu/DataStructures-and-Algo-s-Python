""" Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax
and the built-in sum function."""

print(sum(value*value for value in range(int(input('Enter n value: '))) if value % 2 != 0))