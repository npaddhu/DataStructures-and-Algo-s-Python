'''
R-1.2 Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False
otherwise. However, your function cannot use the multiplication, modulo, or division operators.
'''


def is_even(k):
    """A better solution is to use bitwise operators. We need to check whether last bit is 1 or not.
    If last bit is 1 then the number is odd, otherwise always even."""
    return not(k & 1)


if __name__ == "__main__":
    k = int(input('Enter k value: '))
    print('IsEven: ', is_even(k))


