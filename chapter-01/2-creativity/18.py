"""
Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""


# Method1: pronic numbers (pronic number is the product of two consecutive numbers)
print([i*(i+1) for i in range(10)])

# Method2:
print([i+(i**2) for i in range(10)])
"""
here i+(i**2) is expansion of i*(i+1)
i * (i+1) = i*i + i = i + i**2
"""