"""Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

seq = [pow(2, value) for value in range(int(input('enter n value: '))+1)]
print(seq)
