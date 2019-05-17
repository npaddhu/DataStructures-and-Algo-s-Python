""" Write a short Python function that takes a positive integer n and returns the sum of the squares of all
the positive integers smaller than n. """


def get_sum_of_squares(n):
    """
    # With loop
    sumOfSquares = 0
    for value in range(n):
        sumOfSquares += (value*value)
    return sumOfSquares
    """

    # With formula
    m = n-1 # we nedd the sum of squares less than n
    sumOfSquares = (m * (m+1) * (2*m+1))/6
    return sumOfSquares


if __name__ == '__main__':
    n = int(input('n value: '))
    if n >= 0:
        sumOfSquares = get_sum_of_squares(n)
        print('sum of squares less than: ', sumOfSquares)
    else:
        print('n should be +ve value, re-run the program.')